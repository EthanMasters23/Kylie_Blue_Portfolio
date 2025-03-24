from django import forms
from .models import BookingRequest, ContactRequest

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['name', 'email', 'phone', 'date', 'session_type', 'details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell me more about your request...'}),
        }

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Write your message here...'}),
        }
