from django.db import models
from estudiante.models import Estudiante 

class IntervencionEst(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    fecha_Inicio = models.DateField( verbose_name="Fecha de Ininicio de intervencion")
    fecha_ultima = models.DateField( verbose_name="Fecha de ultima sesión",null=True, blank=True)
    Num_Ses     = models.PositiveIntegerField(default=0,verbose_name="Numero de Sesiones",null=True, blank=True)
    
    class Meta:
        verbose_name = "Intervención Estudiante"
        verbose_name_plural = "Intervenciones Estudiantes"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre+" "+self.Estudiante.apellido

class SesionEst(models.Model):
    id           = models.AutoField(primary_key=True)
    IntervencionEst   = models.ForeignKey(IntervencionEst, verbose_name="Intervencion de Estudiante", on_delete=models.CASCADE)
   # Terapeuta   = models.ForeignKey(Terapeuta, verbose_name="Terapeuta", on_delete=models.CASCADE)
    fecha = models.DateField( verbose_name="Fecha de Sesión")
    
    class Meta:
        verbose_name = "Sesión Estudiante"
        verbose_name_plural = "Sesiones Estudiantes"
        ordering = ['-id']

    def __str__(self):
        return self.IntervencionEst.Estudiante.nombre+" "+self.IntervencionEst.Estudiante.apellido

class SesionD1(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="Sesion de Estudiante", on_delete=models.CASCADE)
    AC1     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas horizontales trazadas en forma entrecortada")
    AC2      = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas horizontales")
    AC3       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas horizontales")
    AC4       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas horizontales grandes y pequeñas")
    AC5       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas horizontales")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    comportamiento  = models.CharField(max_length=20, choices=Calificacion, default=En_Vias, verbose_name="Comportamniento de estudiante en sesión")

    class Meta:
        verbose_name = "Sesion Destreza 1"
        verbose_name_plural = "Sesiones Destrezas 1"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD2(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC6     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 2"
        verbose_name_plural = "Sesiones Destrezas 2"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD3(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC11     = models.PositiveIntegerField(default=0,verbose_name="Completar los círculos trazados de forma entrecortada")
    AC12     = models.PositiveIntegerField(default=0,verbose_name="Completar los semicírculos trazados de forma entrecortada")
    AC13       = models.PositiveIntegerField(default=0,verbose_name="Punzar siguiendo el trazo del círculo")
    AC14       = models.PositiveIntegerField(default=0,verbose_name="Unir los puntos para formar el círculo")
    AC15       = models.PositiveIntegerField(default=0,verbose_name="Seguir el contorno de  bucles ascendentes y descendentes")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 3"
        verbose_name_plural = "Sesiones Destrezas 3"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD4(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC16     = models.PositiveIntegerField(default=0,verbose_name="Completar los cuadrados trazados en forma entrecortada")
    AC17     = models.PositiveIntegerField(default=0,verbose_name="Punzar siguiendo el trazo del cuadrado")
    AC18       = models.PositiveIntegerField(default=0,verbose_name="Unir los puntos para formar el cuadrado")
    AC19       = models.PositiveIntegerField(default=0,verbose_name="Seguir caminos trazados en forma de L")
    AC20       = models.PositiveIntegerField(default=0,verbose_name="Trazar el cuadrado en el papel cuadriculado")
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 4"
        verbose_name_plural = "Sesiones Destrezas 4"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD5(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC21     = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o papel cuadriculado una cruz")
    AC22     = models.PositiveIntegerField(default=0,verbose_name="Unir los puntos trazados para formar una cruz")
    AC23       = models.PositiveIntegerField(default=0,verbose_name="Completar las cruces dibujadas de forma entrecortada")
    AC24       = models.PositiveIntegerField(default=0,verbose_name="Punzar las cruces dibujadas")
    
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 5"
        verbose_name_plural = "Sesiones Destrezas 5"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD6(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC25     = models.PositiveIntegerField(default=0,verbose_name="Completar los triángulos trazados en forma entrecortada")
    AC26     = models.PositiveIntegerField(default=0,verbose_name="Punzar siguiendo el trazo del triángulo")
    AC27       = models.PositiveIntegerField(default=0,verbose_name="Unir los puntos para formar el triángulo")
    AC28       = models.PositiveIntegerField(default=0,verbose_name="Seguir los caminos en zig-zag")
    
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 6"
        verbose_name_plural = "Sesiones Destrezas 6"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD7(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="Sesion Est", on_delete=models.CASCADE)
    AC29     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas onduladas trazadas de forma entrecortada")
    AC30     = models.PositiveIntegerField(default=0,verbose_name="Seguir el trazo de los bucles ascendentes o descendentes")
    AC31       = models.PositiveIntegerField(default=0,verbose_name="Realizar ondas o blucles dentro de dos líneas, sobre ejes horizontales, verticales o inclinados")
    AC32       = models.PositiveIntegerField(default=0,verbose_name="Seguir el trazo de la letra /m/ /n/ manuscrita en forma continua")
    
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 7"
        verbose_name_plural = "Sesiones Destrezas 7"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD8(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="Sesion Est", on_delete=models.CASCADE)
    AC1     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas horizontales trazadas en forma entrecortada")
    AC2      = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas horizontales")
    AC3       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas horizontales")
    AC4       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas horizontales grandes y pequeñas")
    AC5       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas horizontales")
    AC6     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales")     
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 8"
        verbose_name_plural = "Sesiones Destrezas 8"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido

class SesionD9(models.Model):
    id           = models.AutoField(primary_key=True)
    SesionEst   = models.ForeignKey(SesionEst, verbose_name="SesionEst", on_delete=models.CASCADE)
    AC6     = models.PositiveIntegerField(default=0,verbose_name="Completar líneas verticales trazadas en forma entrecortada")
    AC7      = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas verticales y horizontales")
    AC8       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas verticales")
    AC9       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas verticales grandes y pequeñas")
    AC10       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas verticales")     
    AC34       = models.PositiveIntegerField(default=0,verbose_name="Completar líneas oblícuas trazadas en forma entrecortada")
    AC35       = models.PositiveIntegerField(default=0,verbose_name="Seguir laberintos trazando líneas oblicuas")
    AC36       = models.PositiveIntegerField(default=0,verbose_name="Unir dos puntos para formas líneas oblicuas")
    AC37       = models.PositiveIntegerField(default=0,verbose_name="Punzar líneas oblicuas grandes y pequeñas")
    AC48       = models.PositiveIntegerField(default=0,verbose_name="Copiar en la pizarra o en el papel cuadriculado líneas oblicuas")
    AC39       = models.PositiveIntegerField(default=0,verbose_name="Juegos")
    AC40       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC41       = models.PositiveIntegerField(default=0,verbose_name="Dos actividades")
    AC42       = models.PositiveIntegerField(default=0,verbose_name="Juegos serios con lápiz- libre - dos")

    class Meta:
        verbose_name = "Sesion Destreza 9"
        verbose_name_plural = "Sesiones Destrezas 9"
        ordering = ['-id']

    def __str__(self):
        return self.SesionEst.IntervencionEst.Estudiante.nombre+" "+self.SesionEst.IntervencionEst.Estudiante.apellido