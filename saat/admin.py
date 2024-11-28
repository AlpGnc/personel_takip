from django.contrib import admin
from .models import GirisCikisKayit

@admin.register(GirisCikisKayit)
class GirisCikisKayitAdmin(admin.ModelAdmin):
    list_display = ('personel', 'giris_saati', 'cikis_saati')
    list_filter = ('giris_saati',)
    search_fields = ('personel__username',)
