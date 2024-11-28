from rest_framework import serializers
from .models import GirisCikisKayit

class GirisCikisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirisCikisKayit
        fields = '__all__'
