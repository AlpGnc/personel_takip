# saat/urls.py

from django.urls import path
from .views import redirect_user, personel_panel, yetkili_panel

app_name = 'saat'  # Namespace tanımlaması

urlpatterns = [
    path('redirect/', redirect_user, name='redirect_user'),  # Kullanıcıyı yönlendirme
    path('personel-panel/', personel_panel, name='personel_panel'),  # Personel paneli
    path('yetkili-panel/', yetkili_panel, name='yetkili_panel'),  # Yetkili paneli
]
