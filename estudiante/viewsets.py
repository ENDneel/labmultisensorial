from rest_framework import viewsets
from .models import Estudiante
from .serializer import EstudianteSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
