from django.db import models
from django.contrib.auth.models import User

class ItemReport(models.Model):
    ITEM_TYPES = [
        ("LOST", "Lost"),
        ("FOUND", "Found"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLAIMED", "Claimed"),
        ("RESOLVED", "Resolved"),
    ]

    title = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=120)
    item_type = models.CharField(max_length=5, choices=ITEM_TYPES)
    report_date = models.DateField()
    image = models.ImageField(upload_to="items/", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ClaimRequest(models.Model):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    STATES = [(PENDING, 'Pending'), (ACCEPTED, 'Accepted'), (REJECTED, 'Rejected')]
    report = models.ForeignKey(ItemReport, related_name='claims', on_delete=models.CASCADE)
    claimant = models.ForeignKey(User, related_name='item_claims', on_delete=models.CASCADE)
    proof = models.TextField(help_text='Describe private details that prove this item belongs to you.')
    status = models.CharField(max_length=10, choices=STATES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['report', 'claimant'], name='unique_report_claimant')]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.claimant.username} -> {self.report.title}'
