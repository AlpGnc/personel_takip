from django.contrib import admin
from .models import Kullanici

@admin.register(Kullanici)
class KullaniciAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_yetkili')
    list_filter = ('is_staff', 'is_yetkili')
    search_fields = ('username', 'email')
