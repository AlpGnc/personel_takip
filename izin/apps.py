# izin/apps.py

from django.apps import AppConfig

class IzinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'izin'

    def ready(self):
        import izin.signals  # Sinyalleri yükle
