from rest_framework import serializers
from .models import Izin

class IzinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izin
        fields = '__all__'
