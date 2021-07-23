from django.db import models
from estudiante.models import Estudiante

# Create your models here.


class Sesion(models.Model):
    id = models.AutoField(primary_key=True)
    Estudiante = models.ForeignKey(
        Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Sesion")


    MoticidadG = 'Motricidad Gruesa'
    Preescritura = 'Preescritura'
    Escritura = 'Escritura'
    op_area = [
        (MoticidadG, 'Motricidad Gruesa'),
        (Preescritura, 'Preescritura'),
        (Escritura, 'Escritura'),

    ]
    area = models.CharField(max_length=60, choices=op_area,
                            default=MoticidadG, verbose_name="Area")

    class Meta:
        verbose_name = "sesion"
        verbose_name_plural = "sesiones"
        ordering = ['-id']

    def __str__(self):
        return "Estudiante: "+self.Estudiante.nombre + " ID-Ses: "+str(self.id)


class Tablero(models.Model):
    id = models.AutoField(primary_key=True)
    Actividad = models.CharField(max_length=100, verbose_name="Tipo Acividad",)
    Tiempo = models.CharField(max_length=20, verbose_name="Tiempo de Acividad")
    Errores = models.PositiveIntegerField(verbose_name="Numero de Errores")
    datos=models.CharField(max_length=20, verbose_name="Datos recibidos")
    Sesion = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Actividad Tablero"
        verbose_name_plural = "Actividades Tablero"
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
