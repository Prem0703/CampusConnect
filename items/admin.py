from django.contrib import admin
from .models import ItemReport

@admin.register(ItemReport)
class ItemReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'category', 'location', 'report_date', 'status', 'created_by')
    list_filter = ('item_type', 'status', 'category')
    search_fields = ('title', 'description', 'location', 'created_by__username')

from .models import ClaimRequest

@admin.register(ClaimRequest)
class ClaimRequestAdmin(admin.ModelAdmin):
    list_display = ('report', 'claimant', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('report__title', 'claimant__username')
