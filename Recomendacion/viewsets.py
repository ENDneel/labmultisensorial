from rest_framework import viewsets
from .models import RecomendacionEst, RecomendacionD1, RecomendacionD2, RecomendacionD3, RecomendacionD4, RecomendacionD5, RecomendacionD6, RecomendacionD7, RecomendacionD8, RecomendacionD9
from .serializer import RecomendacionEstSerializer, RecomendacionD1Serializer, RecomendacionD2Serializer, RecomendacionD3Serializer, RecomendacionD4Serializer, RecomendacionD5Serializer, RecomendacionD6Serializer, RecomendacionD7Serializer, RecomendacionD8Serializer, RecomendacionD9Serializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
class RecomendacionEstViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionEst.objects.all()
    serializer_class = RecomendacionEstSerializer
class RecomendacionD1ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD1.objects.all()
    serializer_class = RecomendacionD1Serializer

class RecomendacionD2ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD2.objects.all()
    serializer_class = RecomendacionD2Serializer

class RecomendacionD3ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD3.objects.all()
    serializer_class = RecomendacionD3Serializer

class RecomendacionD4ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD4.objects.all()
    serializer_class = RecomendacionD4Serializer

class RecomendacionD5ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD5.objects.all()
    serializer_class = RecomendacionD5Serializer

class RecomendacionD6ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD6.objects.all()
    serializer_class = RecomendacionD6Serializer

class RecomendacionD7ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD7.objects.all()
    serializer_class = RecomendacionD7Serializer

class RecomendacionD8ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD8.objects.all()
    serializer_class = RecomendacionD8Serializer

class RecomendacionD9ViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD9.objects.all()
    serializer_class = RecomendacionD9Serializer