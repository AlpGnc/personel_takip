# saat/models.py

from django.db import models
from kullanici.models import Kullanici
from .utils import calculate_lateness, is_work_day
from django.utils import timezone
from django.utils.timezone import is_naive, make_aware, get_default_timezone

class GirisCikisKayit(models.Model):
    personel = models.ForeignKey(Kullanici, on_delete=models.CASCADE)
    giris_saati = models.DateTimeField(auto_now_add=True)
    cikis_saati = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.personel.username} - Giriş: {self.giris_saati}, Çıkış: {self.cikis_saati or 'Henüz çıkış yapılmadı'}"

    @property
    def lateness(self):
        """Geç kalma süresini hesaplar ve okunabilir formatta döndürür."""
        from .utils import calculate_lateness, is_work_day
        if is_work_day(self.giris_saati.date()):
            lateness = calculate_lateness(self.giris_saati)
            if lateness:
                hours, remainder = divmod(lateness.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                return f"{hours} saat {minutes} dakika"
        return None
    
    @property
    def lateness(self):
        """Geç kalma süresini yalnızca giriş saatine göre hesaplar."""
        from .utils import calculate_lateness, is_work_day

        if is_naive(self.giris_saati):
            self.giris_saati = make_aware(self.giris_saati, get_default_timezone())

        if is_work_day(self.giris_saati.date()):
            lateness = calculate_lateness(self.giris_saati)
            if lateness:
                hours, remainder = divmod(lateness.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                return f"{hours} saat {minutes} dakika"
        return None
