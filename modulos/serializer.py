from .models import Serios
from rest_framework import serializers


class SeriosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Serios
        fields = '__all__'
        