# kullanici/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import personel_ekle

app_name = 'kullanici'  # Namespace tanımlaması

urlpatterns = [
    path('personel-ekle/', personel_ekle, name='personel_ekle'),  # Personel ekleme
    path('personel/login/', LoginView.as_view(template_name='registration/personel_login.html'), name='personel_login'),  # Personel login
    path('yetkili/login/', LoginView.as_view(template_name='registration/yetkili_login.html'), name='yetkili_login'),  # Yetkili login
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout
]
