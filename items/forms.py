from django import forms
from .models import ItemReport

class ItemReportForm(forms.ModelForm):
    class Meta:
        model = ItemReport
        fields = ('title', 'category', 'description', 'location', 'item_type', 'report_date', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Blue water bottle'}),
            'category': forms.TextInput(attrs={'placeholder': 'e.g. Bottle, ID card, Books'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add useful details to help identify the item'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Library, Canteen, Lab 2'}),
            'item_type': forms.Select(),
            'report_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(),
        }
