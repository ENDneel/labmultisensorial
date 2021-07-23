from rest_framework import viewsets
from .models import IntervencionEst, SesionEst, SesionD1, SesionD2, SesionD3, SesionD4, SesionD5, SesionD6, SesionD7, SesionD8, SesionD9
from .serializer import IntervencionEstSerializer, SesionEstSerializer,SesionD1Serializer, SesionD2Serializer, SesionD3Serializer, SesionD4Serializer, SesionD5Serializer, SesionD6Serializer, SesionD7Serializer, SesionD8Serializer, SesionD9Serializer

class IntervencionEstViewSet(viewsets.ModelViewSet):
    queryset = IntervencionEst.objects.all()
    serializer_class = IntervencionEstSerializer

class SesionEstViewSet(viewsets.ModelViewSet):
    queryset = SesionEst.objects.all()
    serializer_class = SesionEstSerializer

class SesionD1ViewSet(viewsets.ModelViewSet):
    queryset = SesionD1.objects.all()
    serializer_class = SesionD1Serializer

class SesionD2ViewSet(viewsets.ModelViewSet):
    queryset = SesionD2.objects.all()
    serializer_class = SesionD2Serializer

class SesionD3ViewSet(viewsets.ModelViewSet):
    queryset = SesionD3.objects.all()
    serializer_class = SesionD3Serializer

class SesionD4ViewSet(viewsets.ModelViewSet):
    queryset = SesionD4.objects.all()
    serializer_class = SesionD4Serializer

class SesionD5ViewSet(viewsets.ModelViewSet):
    queryset = SesionD5.objects.all()
    serializer_class = SesionD5Serializer

class SesionD6ViewSet(viewsets.ModelViewSet):
    queryset = SesionD6.objects.all()
    serializer_class = SesionD6Serializer

class SesionD7ViewSet(viewsets.ModelViewSet):
    queryset = SesionD7.objects.all()
    serializer_class = SesionD7Serializer

class SesionD8ViewSet(viewsets.ModelViewSet):
    queryset = SesionD8.objects.all()
    serializer_class = SesionD8Serializer

class SesionD9ViewSet(viewsets.ModelViewSet):
    queryset = SesionD9.objects.all()
    serializer_class = SesionD9Serializer