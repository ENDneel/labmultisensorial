from .models import IntervencionEst, SesionEst, SesionD1, SesionD2, SesionD3, SesionD4, SesionD5, SesionD6, SesionD7, SesionD8, SesionD9
from rest_framework import serializers


class IntervencionEstSerializer(serializers.ModelSerializer):
    class Meta:
        model=IntervencionEst
        fields = '__all__'

class SesionEstSerializer(serializers.ModelSerializer):
    class Meta:
        model=SesionEst
        fields = '__all__'

class SesionD1Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD1
        fields = '__all__'

class SesionD2Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD2
        fields = '__all__'


class SesionD3Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD3
        fields = '__all__'

class SesionD4Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD4
        fields = '__all__'

class SesionD5Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD5
        fields = '__all__'

class SesionD6Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD6
        fields = '__all__'

class SesionD7Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD7
        fields = '__all__'

class SesionD8Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD8
        fields = '__all__'

class SesionD9Serializer(serializers.ModelSerializer):
    class Meta:
        model=SesionD9
        fields = '__all__'
