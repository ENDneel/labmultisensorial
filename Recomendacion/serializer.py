from .models import RecomendacionEst, RecomendacionD1, RecomendacionD2, RecomendacionD3, RecomendacionD4, RecomendacionD5, RecomendacionD6, RecomendacionD7, RecomendacionD8, RecomendacionD9
from rest_framework import serializers


class RecomendacionEstSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionEst
        fields = '__all__'
        
class RecomendacionD1Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD1
        fields = '__all__'

class RecomendacionD2Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD2
        fields = '__all__'

class RecomendacionD3Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD3
        fields = '__all__'

class RecomendacionD4Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD4
        fields = '__all__'

class RecomendacionD5Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD5
        fields = '__all__'

class RecomendacionD6Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD6
        fields = '__all__'

class RecomendacionD7Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD7
        fields = '__all__'

class RecomendacionD8Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD8
        fields = '__all__'

class RecomendacionD9Serializer(serializers.ModelSerializer):
    class Meta:
        model=RecomendacionD9
        fields = '__all__'