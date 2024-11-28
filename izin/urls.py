# izin/urls.py

from django.urls import path
from . import views

app_name = 'izin'

urlpatterns = [
    path('talep-et/', views.izin_talep_et, name='izin_talep_et'),
    path('onayla/', views.izin_onayla, name='izin_onayla'),
]
