from django.db.models import fields
from .models import Sesion,Tablero
from rest_framework import serializers

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sesion
        fields = '__all__'
        
class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tablero
        fields = '__all__'


class SerializerData(serializers.ModelSerializer):
    tablero=TableroSerializer()
    class Meta:
        model = Sesion
        fields=['id','tablero']


