from django import forms
from .models import LeadCapture


class LeadCaptureForm(forms.ModelForm):
    class Meta:
        model = LeadCapture
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ihre E-Mail-Adresse',
                'class': 'w-full px-4 py-3 border border-py-navy/20 bg-white text-py-text focus:border-py-gold focus:outline-none',
                'required': True,
            })
        }
