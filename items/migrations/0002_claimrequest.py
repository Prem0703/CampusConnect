from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [('items', '0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='ClaimRequest', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('proof', models.TextField(help_text='Describe private details that prove this item belongs to you.')),
            ('status', models.CharField(choices=[('PENDING','Pending'),('ACCEPTED','Accepted'),('REJECTED','Rejected')], default='PENDING', max_length=10)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('claimant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_claims', to=settings.AUTH_USER_MODEL)),
            ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='items.itemreport')),
        ], options={'ordering':['-created_at']}),
        migrations.AddConstraint(model_name='claimrequest', constraint=models.UniqueConstraint(fields=('report','claimant'), name='unique_report_claimant')),
    ]
