from .models import EvaluacionD, EvaluacionD1, EvaluacionD2, EvaluacionD3, EvaluacionD4, EvaluacionD5, EvaluacionD6, EvaluacionD7, EvaluacionD8, EvaluacionD9
from rest_framework import serializers


class EvaluacionDSerializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD
        fields = '__all__'


class EvaluacionD1Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD1
        fields = '__all__'

class EvaluacionD2Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD2
        fields = '__all__'

class EvaluacionD3Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD3
        fields = '__all__'

class EvaluacionD4Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD4
        fields = '__all__'

class EvaluacionD5Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD5
        fields = '__all__'

class EvaluacionD6Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD6
        fields = '__all__'

class EvaluacionD7Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD7
        fields = '__all__'

class EvaluacionD8Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD8
        fields = '__all__'

class EvaluacionD9Serializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionD9
        fields = '__all__'
