from django.db import models
from django.utils import tree

from estudiante.models import Estudiante

# Create your models here.


class Serios(models.Model):
    id = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE,null=True)
    fecha = models.CharField(max_length=30, verbose_name="fecha",null=True)
    actividad=models.CharField(max_length=30,verbose_name="actividad",null=True)
    duracion = models.PositiveIntegerField(default=0, verbose_name="duracion")
    class Meta:
        ordering = ['id']
    def __str__(self):   
        return self.id
