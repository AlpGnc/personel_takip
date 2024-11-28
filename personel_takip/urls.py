# personel_takip/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kullanici/', include(('kullanici.urls', 'kullanici'), namespace='kullanici')),
    path('saat/', include(('saat.urls', 'saat'), namespace='saat')),
    path('izin/', include(('izin.urls', 'izin'), namespace='izin')),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
]
