from xml.parsers.expat import model
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

class Modulos(models.Model):
    estado_op = [
        ('Activo', 'Activo'),
        ('Desactivo', 'Desactivo'),
    ]
    nombre=models.CharField(max_length=30,verbose_name="NombreModulo")
    mac=models.CharField(max_length=11,verbose_name="MAC",primary_key=True)
    estado=models.CharField(max_length=10,choices=estado_op,default="Desactivo",verbose_name='Estado')
    bateria=models.CharField(max_length=4,verbose_name='Bateria')

    class Meta:
        def __str__(self) :
            return str(self.mac)