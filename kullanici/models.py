# kullanici/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Kullanici(AbstractUser):
    is_yetkili = models.BooleanField(default=False)  # Yetkili kullanıcıları ayırt etmek için
    annual_leave_balance = models.IntegerField(default=15)  # Yıllık izin bakiyesi

    def __str__(self):
        return self.username
