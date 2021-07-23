from django.db import models
from estudiante.models import Estudiante 

class RecomendacionEst(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Recomendación Estudiante"
        verbose_name_plural = "Recomendación Estudiante"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre

class RecomendacionD1(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="Estudiante", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField( verbose_name="Numero semanas")
    AC1     = models.PositiveIntegerField(verbose_name="Completar líneas horizontales trazadas en forma entrecortada")
    AC2      = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas horizontales")
    AC3       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas horizontales")
    AC4       = models.PositiveIntegerField(verbose_name="Punzar líneas horizontales grandes y pequeñas")
    AC5       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas horizontales")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 1"
        verbose_name_plural = "Recomendaciones Destreza 1"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD2(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC6     = models.PositiveIntegerField(verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 2"
        verbose_name_plural = "Recomendaciones Destreza 2"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD3(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC11     = models.PositiveIntegerField(verbose_name="Completar los círculos trazados de forma entrecortada")
    AC12     = models.PositiveIntegerField(verbose_name="Completar los semicírculos trazados de forma entrecortada")
    AC13       = models.PositiveIntegerField(verbose_name="Punzar siguiendo el trazo del círculo")
    AC14       = models.PositiveIntegerField(verbose_name="Unir los puntos para formar el círculo")
    AC15       = models.PositiveIntegerField(verbose_name="Seguir el contorno de  bucles ascendentes y descendentes")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 3"
        verbose_name_plural = "Recomendaciones Destreza 3"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD4(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField( verbose_name="Numero semanas")
    AC16     = models.PositiveIntegerField(verbose_name="Completar los cuadrados trazados en forma entrecortada")
    AC17     = models.PositiveIntegerField(verbose_name="Punzar siguiendo el trazo del cuadrado")
    AC18       = models.PositiveIntegerField(verbose_name="Unir los puntos para formar el cuadrado")
    AC19       = models.PositiveIntegerField(verbose_name="Seguir caminos trazados en forma de L")
    AC20       = models.PositiveIntegerField(verbose_name="Trazar el cuadrado en el papel cuadriculado")
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 4"
        verbose_name_plural = "Recomendaciones Destreza 4"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD5(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField( verbose_name="Numero semanas")
    AC21     = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o papel cuadriculado una cruz")
    AC22     = models.PositiveIntegerField(verbose_name="Unir los puntos trazados para formar una cruz")
    AC23       = models.PositiveIntegerField(verbose_name="Completar las cruces dibujadas de forma entrecortada")
    AC24       = models.PositiveIntegerField(verbose_name="Punzar las cruces dibujadas")
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 5"
        verbose_name_plural = "Recomendaciones Destreza 5"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD6(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC25     = models.PositiveIntegerField(verbose_name="Completar los triángulos trazados en forma entrecortada")
    AC26     = models.PositiveIntegerField(verbose_name="Punzar siguiendo el trazo del triángulo")
    AC27       = models.PositiveIntegerField(verbose_name="Unir los puntos para formar el triángulo")
    AC28       = models.PositiveIntegerField(verbose_name="Seguir los caminos en zig-zag")
    
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 6"
        verbose_name_plural = "Recomendaciones Destreza 6"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD7(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="Recomendacion Est", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC29     = models.PositiveIntegerField(verbose_name="Completar líneas onduladas trazadas de forma entrecortada")
    AC30     = models.PositiveIntegerField(verbose_name="Seguir el trazo de los bucles ascendentes o descendentes")
    AC31       = models.PositiveIntegerField(verbose_name="Realizar ondas o blucles dentro de dos líneas, sobre ejes horizontales, verticales o inclinados")
    AC32       = models.PositiveIntegerField(verbose_name="Seguir el trazo de la letra /m/ /n/ manuscrita en forma continua")
    
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 7"
        verbose_name_plural = "Recomendaciones Destreza 7"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD8(models.Model):
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="Recomendacion Est", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC1     = models.PositiveIntegerField(verbose_name="Completar líneas horizontales trazadas en forma entrecortada")
    AC2      = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas horizontales")
    AC3       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas horizontales")
    AC4       = models.PositiveIntegerField(verbose_name="Punzar líneas horizontales grandes y pequeñas")
    AC5       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas horizontales")
    AC6     = models.PositiveIntegerField(verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales") 
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Recomendacion Destreza 8"
        verbose_name_plural = "Recomendaciones Destreza 8"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre

class RecomendacionD9(models.Model):  
    id           = models.AutoField(primary_key=True)
    RecomendacionEst   = models.ForeignKey(RecomendacionEst, verbose_name="RecomendacionEst", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Semanas       = models.PositiveIntegerField(verbose_name="Numero semanas")
    AC6     = models.PositiveIntegerField(verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales")     
    AC34       = models.PositiveIntegerField(verbose_name="Completar líneas oblícuas trazadas en forma entrecortada")
    AC35       = models.PositiveIntegerField(verbose_name="Seguir laberintos trazando líneas oblicuas")
    AC36       = models.PositiveIntegerField(verbose_name="Unir dos puntos para formas líneas oblicuas")
    AC37       = models.PositiveIntegerField(verbose_name="Punzar líneas oblicuas grandes y pequeñas")
    AC38       = models.PositiveIntegerField(verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas oblicuas")
    AC39       = models.PositiveIntegerField(verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(verbose_name="Juegos serios con lápiz- libre - dos")
    AC43       = models.PositiveIntegerField(verbose_name="Juegos serios: topos y otro")
    class Meta:
        verbose_name = "Recomendacion Destreza 9"
        verbose_name_plural = "Recomendaciones Destreza 9"
        ordering = ['-id']

    def __str__(self):
        return self.RecomendacionEst.Estudiante.nombre