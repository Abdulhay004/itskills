from django import forms
from .models import Internship, InProgress, Components, IconPack, DesignNewChanges, MobileApp, MobileAppWireframe

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['company_name', 'position', 'requirements', 'duration']