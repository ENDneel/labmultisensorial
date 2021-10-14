
from rest_framework import viewsets
from .models import Sesion, Tablero
from .serializer import SesionSerializer, TableroSerializer

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer