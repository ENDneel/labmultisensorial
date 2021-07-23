from rest_framework import viewsets
from .models import *
from .serializers import * 

class RecomendacionD1SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD1S.objects.all()
    serializer_class = RecomendacionD1SSerializer

class RecomendacionD2SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD2S.objects.all()
    serializer_class = RecomendacionD2SSerializer

class RecomendacionD3SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD3S.objects.all()
    serializer_class = RecomendacionD3SSerializer

class RecomendacionD4SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD4S.objects.all()
    serializer_class = RecomendacionD4SSerializer

class RecomendacionD5SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD5S.objects.all()
    serializer_class = RecomendacionD5SSerializer

class RecomendacionD6SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD6S.objects.all()
    serializer_class = RecomendacionD6SSerializer

class RecomendacionD7SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD7S.objects.all()
    serializer_class = RecomendacionD7SSerializer

class RecomendacionD8SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD8S.objects.all()
    serializer_class = RecomendacionD8SSerializer

class RecomendacionD9SViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionD9S.objects.all()
    serializer_class = RecomendacionD9SSerializer