# izin/models.py

from django.db import models
from django.conf import settings

class Izin(models.Model):
    ONAY_DURUMU_CHOICES = [
        ('Bekliyor', 'Bekliyor'),
        ('Onaylandı', 'Onaylandı'),
        ('Reddedildi', 'Reddedildi'),
    ]

    personel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    onay_durumu = models.CharField(max_length=20, choices=ONAY_DURUMU_CHOICES, default='Bekliyor')

    def __str__(self):
        return f"{self.personel.username} - {self.baslangic_tarihi} to {self.bitis_tarihi} - {self.onay_durumu}"
