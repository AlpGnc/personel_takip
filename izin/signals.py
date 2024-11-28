# izin/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from kullanici.models import Kullanici
from .models import Izin
import datetime

@receiver(post_save, sender=Kullanici)
def create_initial_izin(sender, instance, created, **kwargs):
    if created:
        # Yeni kullanıcı oluşturulduğunda otomatik izin tanımla
        Izin.objects.create(
            personel=instance,
            baslangic_tarihi=datetime.date.today(),
            bitis_tarihi=datetime.date.today() + datetime.timedelta(days=15),
            onay_durumu='Onaylandı'
        )
