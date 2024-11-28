# kullanici/forms.py

from django import forms
from .models import Kullanici

class PersonelEkleForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Kullanici
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_yetkili = False  # Personel olarak işaretle
        user.is_staff = False  # Yönetici yetkisi yok
        user.set_password(self.cleaned_data['password'])  # Şifreyi hashle
        if commit:
            user.save()
        return user
