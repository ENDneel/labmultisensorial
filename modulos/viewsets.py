from rest_framework import viewsets

from modulos.serializer import SeriosSerializer
from .models import Serios



class SeriosViewSet(viewsets.ModelViewSet):
    queryset = Serios.objects.all()
    serializer_class = SeriosSerializer
