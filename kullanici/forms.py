from django import forms
from .models import Kullanici

class PersonelEkleForm(forms.ModelForm):
    # Şifre alanı
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    # Role seçim alanı
    role = forms.ChoiceField(
        choices=[('personel', 'Personel'), ('yetkili', 'Yetkili')],
        required=True,
        label="Rol Seçin"
    )

    class Meta:
        model = Kullanici
        fields = ['username', 'email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Seçilen role göre kullanıcıyı işaretle
        role = self.cleaned_data['role']
        if role == 'yetkili':
            user.is_yetkili = True  # Yetkili olarak işaretle
            user.is_staff = True  # Yönetici yetkisi ver
        else:
            user.is_yetkili = False  # Personel olarak işaretle
            user.is_staff = False  # Yönetici yetkisi yok
        
        # Şifreyi hashle
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        
        return user
