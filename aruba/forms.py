from django import forms

from .models import Participants

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Participants
        fields = ['email']