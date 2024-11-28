from django.contrib import admin
from .models import Izin

@admin.register(Izin)
class IzinAdmin(admin.ModelAdmin):
    list_display = ('personel', 'baslangic_tarihi', 'bitis_tarihi', 'onay_durumu')
    list_filter = ('onay_durumu',)
    search_fields = ('personel__username',)
