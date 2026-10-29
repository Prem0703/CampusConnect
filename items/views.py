from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.db.models import Q
from django.views.decorators.http import require_POST
from .forms import ItemReportForm
from .models import ItemReport, ClaimRequest

def home(request):
    reports = ItemReport.objects.select_related('created_by').order_by('-created_at')
    item_type = request.GET.get('type', '').upper()
    query = request.GET.get('q', '').strip()
    if item_type in ('LOST', 'FOUND'):
        reports = reports.filter(item_type=item_type)
    if query:
        reports = reports.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query))
    return render(request, 'items/home.html', {'reports': reports, 'active_type': item_type, 'query': query, 'lost_count': ItemReport.objects.filter(item_type='LOST', status='OPEN').count(), 'found_count': ItemReport.objects.filter(item_type='FOUND', status='OPEN').count()})

@login_required
def report_create(request):
    if request.method == 'POST':
        form = ItemReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            messages.success(request, 'Your report has been posted!')
            return redirect('report_detail', pk=report.pk)
    else:
        form = ItemReportForm()
    return render(request, 'items/report_form.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome to CampusConnect!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'items/signup.html', {'form': form})

def report_detail(request, pk):
    report = get_object_or_404(ItemReport.objects.select_related('created_by'), pk=pk)
    is_owner = request.user.is_authenticated and request.user.pk == report.created_by_id
    my_claim = ClaimRequest.objects.filter(report=report, claimant=request.user).first() if request.user.is_authenticated and not is_owner else None
    claims = report.claims.select_related('claimant') if is_owner else []
    return render(request, 'items/report_detail.html', {'report': report, 'is_owner': is_owner, 'my_claim': my_claim, 'claims': claims})

@login_required
@require_POST
def claim_item(request, pk):
    report = get_object_or_404(ItemReport, pk=pk)
    if report.created_by_id == request.user.pk or report.status != 'OPEN':
        messages.error(request, 'This item cannot be claimed.')
        return redirect('report_detail', pk=pk)
    proof = request.POST.get('proof', '').strip()
    if len(proof) < 15 or len(proof) > 1500:
        messages.error(request, 'Please give 15–1500 characters of identifying details.')
        return redirect('report_detail', pk=pk)
    claim, created = ClaimRequest.objects.get_or_create(report=report, claimant=request.user, defaults={'proof': proof})
    messages.success(request, 'Claim request sent to the report creator.' if created else 'You already sent a claim for this item.')
    return redirect('report_detail', pk=pk)

@login_required
@require_POST
def review_claim(request, pk, claim_id):
    with transaction.atomic():
        report = get_object_or_404(ItemReport.objects.select_for_update(), pk=pk, created_by=request.user)
        claim = get_object_or_404(ClaimRequest.objects.select_for_update(), pk=claim_id, report=report)
        action = request.POST.get('action')
        if report.status != 'OPEN' or claim.status != 'PENDING' or action not in ('accept', 'reject'):
            messages.error(request, 'This request can no longer be changed.')
        elif action == 'accept':
            claim.status = 'ACCEPTED'
            claim.save(update_fields=['status'])
            report.status = 'CLAIMED'
            report.save(update_fields=['status'])
            report.claims.filter(status='PENDING').exclude(pk=claim.pk).update(status='REJECTED')
            messages.success(request, 'Claim accepted. Verify identity before returning the item.')
        else:
            claim.status = 'REJECTED'
            claim.save(update_fields=['status'])
            messages.success(request, 'Claim rejected.')
    return redirect('report_detail', pk=pk)

@login_required
@require_POST
def mark_returned(request, pk):
    report = get_object_or_404(ItemReport, pk=pk, created_by=request.user)
    if report.status == 'CLAIMED' and report.claims.filter(status='ACCEPTED').exists():
        report.status = 'RESOLVED'
        report.save(update_fields=['status'])
        messages.success(request, 'Item marked as returned!')
    else:
        messages.error(request, 'Accept a claim before marking the item returned.')
    return redirect('report_detail', pk=pk)
