from rest_framework import viewsets
from .models import EvaluacionD, EvaluacionD1, EvaluacionD2, EvaluacionD3, EvaluacionD4, EvaluacionD5, EvaluacionD6, EvaluacionD7, EvaluacionD8, EvaluacionD9
from .serializer import EvaluacionDSerializer, EvaluacionD1Serializer, EvaluacionD2Serializer, EvaluacionD3Serializer, EvaluacionD4Serializer, EvaluacionD5Serializer, EvaluacionD6Serializer, EvaluacionD7Serializer, EvaluacionD8Serializer, EvaluacionD9Serializer
from Recomendacion.models import RecomendacionEst
from rest_framework.decorators import action


class EvaluacionDViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD.objects.all()
    serializer_class = EvaluacionDSerializer


class EvaluacionD1ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD1.objects.all()
    serializer_class = EvaluacionD1Serializer

class EvaluacionD2ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD2.objects.all()
    serializer_class = EvaluacionD2Serializer

class EvaluacionD3ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD3.objects.all()
    serializer_class = EvaluacionD3Serializer

class EvaluacionD4ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD4.objects.all()
    serializer_class = EvaluacionD4Serializer

class EvaluacionD5ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD5.objects.all()
    serializer_class = EvaluacionD5Serializer

class EvaluacionD6ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD6.objects.all()
    serializer_class = EvaluacionD6Serializer

class EvaluacionD7ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD7.objects.all()
    serializer_class = EvaluacionD7Serializer

class EvaluacionD8ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD8.objects.all()
    serializer_class = EvaluacionD8Serializer

class EvaluacionD9ViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionD9.objects.all()
    serializer_class = EvaluacionD9Serializer