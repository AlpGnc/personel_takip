from rest_framework import serializers
from .models import Kullanici

class KullaniciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ['id', 'username', 'email', 'is_yetkili', 'is_staff']
