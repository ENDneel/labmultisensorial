from django.db import models
from estudiante.models import Estudiante

class EvaluacionD(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante Evaluado", on_delete=models.CASCADE)
    Fecha        = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Evaluacion Estudiante"
        verbose_name_plural = "Evaluaciones Estudiantes"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre

class EvaluacionD1(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En vias de logro'),
        (No_Logrado, 'No logrado'),
    ]
    D1  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA LINEA HORIZONTAL")
   
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 1"
        verbose_name_plural = "Evaluaciones Destreza 1"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD2(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D2  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA LINEA VERTICAL")
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 2"
        verbose_name_plural = "Evaluaciones Destreza 2"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD3(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D3  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA CIRCUNFERENCIA")
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 3"
        verbose_name_plural = "Evaluaciones Destreza 3"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD4(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D4  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA CUADRADO")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 4"
        verbose_name_plural = "Evaluaciones Destreza 4"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD5(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D5  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA CRUZ")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 5"
        verbose_name_plural = "Evaluaciones Destreza 5"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD6(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D6  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA TRIANGULO")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 6"
        verbose_name_plural = "Evaluaciones Destreza 6"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD7(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D7  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="DIBUJA ONDULADA")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 7"
        verbose_name_plural = "Evaluaciones Destreza 7"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD8(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D8  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="PENDIENTE LETRAS")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 8"
        verbose_name_plural = "Evaluaciones Destreza 8"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre

class EvaluacionD9(models.Model):
    id           = models.AutoField(primary_key=True)
    EvaluacionD   = models.ForeignKey(EvaluacionD, verbose_name="Evaluación", on_delete=models.CASCADE)
    LOGRADO    = 'Logrado'
    En_Vias   = 'En vias de logro'
    No_Logrado = 'No logrado'
    Calificacion = [
        (LOGRADO, 'Logrado'),
        (En_Vias, 'En proceso'),
        (No_Logrado, 'No logrado'),
    ]
    D9  = models.CharField(max_length=20, choices=Calificacion, default=LOGRADO, verbose_name="PENDIENTE NUMEROS")
    
    NORMAL    = 'Normal'
    HIPERTONICO   = 'Hipertónico'
    HIPOTONICO = 'Hipotónico'
    Calificacion1 = [
        (NORMAL, 'Normal'),
        (HIPERTONICO, 'Hipertónico'),
        (HIPOTONICO, 'Hipotónico'), ]
    
    D10  = models.CharField(max_length=20, choices=Calificacion1, default=NORMAL, verbose_name="PRESION SOBRE EL PAPEL")
    
    TRIDIGITAL    = 'Tridigital'
    DIGITAL   = 'Digital'
    MODAL = 'Modal'
    Calificacion2 = [
        (TRIDIGITAL, 'Tridigital'),
        (DIGITAL, 'Digital'),
        (MODAL, 'Modal'),
    ] 
    D11  = models.CharField(max_length=20, choices=Calificacion2, default=TRIDIGITAL, verbose_name="TIPO DE AGARRE")
    
    BUENA    = 'Buena'
    MALA   = 'Mala'
    Calificacion3 = [
        (BUENA, 'Buena'),
        (MALA, 'Mala'),
    ]
    D12  = models.CharField(max_length=20, choices=Calificacion3, default=BUENA, verbose_name="DIRECCIONALIDAD")
    
    NO_ESTRESADO    = 'No estresado'
    ESTRESADO   = 'Estresado'
    Calificacion4 = [
        (NO_ESTRESADO, 'No estresado'),
        (ESTRESADO, 'Estresado'),
    ]
    D13  = models.CharField(max_length=20, choices=Calificacion4, default=NO_ESTRESADO, verbose_name="ESTADO DE ANIMO")
    
    PRONACION_SUPINACION    = 'Pronacion supinacion'
    MOVIMIENTO_PALMAR   = 'Movimiento Palmar'
    Calificacion5 = [
        (PRONACION_SUPINACION, 'Pronacion supinacion'),
        (MOVIMIENTO_PALMAR, 'Movimiento Palmar'),
    ]
    D14  = models.CharField(max_length=20, choices=Calificacion5, default=PRONACION_SUPINACION, verbose_name="MOVIMIENTO MANO DEDOS")
    	
    class Meta:
        verbose_name = "Evaluacion Destreza 9"
        verbose_name_plural = "Evaluaciones Destreza 9"
        ordering = ['-id']

    def __str__(self):
        return self.EvaluacionD.Estudiante.nombre
