# saat/forms.py

from django import forms
from .models import GirisCikisKayit

class GirisCikisForm(forms.ModelForm):
    class Meta:
        model = GirisCikisKayit
        fields = ['cikis_saati']
        widgets = {
            'cikis_saati': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
