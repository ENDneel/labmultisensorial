from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Estudiante(models.Model):
    id      = models.AutoField(primary_key=True)
    #Terapeuta =models.ForeignKey(Terapeuta, verbose_name="Terapeuta", on_delete=models.CASCADE, null=True,blank=True) 
    nombre  = models.CharField(max_length=100, verbose_name="Nombre")
    apellido  = models.CharField(max_length=100, verbose_name="Apellido")
    edad_Cronologica = models.PositiveIntegerField(blank=True, null=True, default=0,verbose_name="Edad Cronologica", )
    edad_Mental = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="Edad Mental")
    opciones_Educacion = [
        ('No Escolarizado' , 'No Escolarizado'),
        ('Educacion Inicial' , 'Educacion Inicial'),
        ( 'Educacion Basica' , 'Educacion Basica'),
    ]
    grado_Educacion  = models.CharField(max_length=50, choices=opciones_Educacion, default='Educacion Inicial', verbose_name="Grado de Educacionn")
    MASCULINO = 'Masculino'
    FEMENINO  = 'Femenino'
    SEXO_Option = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_Option, default=MASCULINO, verbose_name="Sexo")
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['id']

    def __str__(self):   
        return self.nombre

class Formulario(models.Model):
    Estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    op_discapacidad_intelectual_auditiva=[('No presenta','No presenta'),('Leve','Leve'),('Moderado','Moderado'),('Severo','Severo'),('Profundo','Profundo')]
    op_discapacidad_visual=[('No presenta','No presenta'),('Leve','Leve'),('Moderado','Moderado'),('Severo','Severo'),('Total','Total')]
    op_discapacidad_motriz=[('No presenta','No presenta'),('Leve','Leve'),('Moderado','Moderado'),('Severo','Severo')]
    op_discapacioda_pci=[('No presenta','No presenta'),('Espástica','Espástica'),('Atetósica','Atetósica'),('Atáxica','Atáxica'),('Mixta','Mixta ')]
    op_discapacidad_auditiva_prof=[('No presenta','No presenta'),('Unilateral','Unilateral'),('Bilateral','Bilatera')]
    op_discapacidad_pci_prof=[('No presenta','No presenta'),('Monoplejía','Monoplejía'),('Hemiplejía','Hemiplejía'),('Paraplejía','Paraplejía'),('Triplejía','Triplejía'),('Tetraplejía','Tetraplejía')]
    opcion=[('Si','Si'),('No','No')]
    op_control_cuerpo=[('A1','Mantiene el control total de su cuerpo'),('A2','Mantiene el control de su cuerpo con dificultad en el equilibrio y le gustan las actividades de motricidad gruesa',),
    ('A3','Mantiene el control de su cuerpo con dificultad en el equilibrio y no le gustan las actividades de motricidad gruesa'),
    ('A4','Mantiene el control de su cuerpo, pero le cuesta realizar actividades de motricidad gruesa'),('A5','No mantiene el control de su cuerpo, necesita apoyo y supervisión total')]
    op_cord_oculo_manual=[('B1','Buena coordinación óculo manual'),('B2','Dificultad en mantener la coordinación óculo manual')]
    op_atencion=[('C1','Mantiene la atención durante una tarea asignada'),('C2','Mantiene la atención durante una tarea asignada a pesar que se demora, pero la culmina'),
    ('C3','La mayoría de las veces mantiene la atención en una tarea asignada'),('C4','Le cuesta mantener la atención en una tarea asignada, se distrae con facilidad'),
    ('C5','Le cuesta mantener la atención en una tarea asignada, quiere terminarla rápido'),('C6','Mantiene la atención por períodos cortos en objetos con luces y sonidos')]
    op_lateralidad=[('D1','Definida'),('D2','Cambia de mano constantemente al realizar una actividad'),('D3','Cambia de mano en pocas ocasiones, pero utiliza más una mano')]
    op_diso_manos=[('E1','Utiliza constantemente la mano de apoyo'),('E2','Utiliza a veces la mano de apoyo'),('E3','No utiliza la mano de apoyo')]
    op_predis_tarea_mesa=[('F1','Permanece sentado durante una tarea'),('F2','Le cuesta mantenerse sentado en una tarea'),('F3','No permanece sentado')]
    op_manipulacion_lapiz=[('G1','Le atraen los lápices y los manipula'),('G2','Le atraen poco los lápices y los manipula poco'),('G3','No le atraen los lápices ni los manipula'),
    ('G4','No le atraen los lápices ni los manipula a menos de que sean necesarios en la tarea asignada')]
    op_sensi_tacto=[('H1','Tolera actividades que implican ensuciarse y mojarse las manos'),('H2','Tolera poco las actividades que implican ensuciarse o mojarse las manos'),
    ('H3','No tolera actividades que implican ensuciarse o mojarse las manos')]
    op_len_comprensivo=[('A1','Tiene buena comprensión'),('A2','Su comprensión es buena, pero necesita de apoyos visuales y señas'),('A3','Su comprensión es regular, hay que repetirle algunas veces la consigna'),
    ('A4','Su comprensión es regular a pesar de repetirle verbalmente necesita de apoyos visuales.'),('A5','Su comprensión es mala, responde por reflejos')]
    op_len_expresivo=[('B1','Tiene buen lenguaje expresivo'),('B2','Su lenguaje es claro, rígido, repetitivo y le cuesta participar en conversaciones'),('B3','Se expresa mediante el lenguaje oral con una cierta distorsión en la entonación de la voz'),
    ('B4','Se expresa mediante sonidos guturales, gritos y llanto'),('B5','Se expresa mediante lenguaje oral, pero tiene dificultad en pronunciar claramente'),('B6','Se expresa mediante lenguaje oral con palabras monosílabas y bisílabas'),
    ('B7','Se expresa mediante Sistemas Alternativos y Aumentativos de Comunicación (pictogramas)'),('B8','Se expresa mediante lenguaje de señas y Sistemas Alternativos y Aumentativos de Comunicación')]
    #Discapcidades
    id      = models.AutoField(primary_key=True)
    disc_intelectual_grado=models.CharField(max_length=50, choices=op_discapacidad_intelectual_auditiva, verbose_name="Discapacidad Intelectual",default='No presenta')
    disc_visual_grado=models.CharField(max_length=50, choices=op_discapacidad_visual, default='No presenta', verbose_name="Discapacidad Visual")
    disc_motriz_grado=models.CharField(max_length=50,choices=op_discapacidad_motriz,default='No presenta')
    disc_auditiva_grado=models.CharField(max_length=50,choices=op_discapacidad_intelectual_auditiva,default='No presenta')
    disc_auditiva_profundidad=models.CharField(max_length=50,choices=op_discapacidad_auditiva_prof,default='No presenta')
    disc_pci_grado=models.CharField(max_length=50,choices=op_discapacioda_pci,default='No presenta')
    disc_pci_profundidad=models.CharField(max_length=50,choices=op_discapacidad_pci_prof,default='No presenta')

    #sindromes
    sindrome_down=models.CharField(max_length=2,choices=opcion,default='No')
    sindrome_lennon=models.CharField(max_length=2,choices=opcion,default='No')
    sindrome_te=models.CharField(max_length=2,choices=opcion,default='No')
    sindorme_tdah=models.CharField(max_length=2,choices=opcion,default='No')
    transtorno_agresivo=models.CharField(max_length=2,choices=opcion,default='No')
    #CARACTERÍSTICAS DE ELEMENTOS GRAFOMOTRICES 
    control_cuerpo=models.CharField(max_length=2,choices=op_control_cuerpo,default='A1')
    cord_oculo_manual=models.CharField(max_length=2,choices=op_cord_oculo_manual,default='B1')
    atencion=models.CharField(max_length=2,choices=op_atencion,default='C1')
    lateralidad=models.CharField(max_length=2,choices=op_lateralidad,default='D1')
    disociacion_manos=models.CharField(max_length=2,choices=op_diso_manos,default='E1')
    predispo_mesa=models.CharField(max_length=2,choices=op_predis_tarea_mesa,default='F1')
    manipulacion_lapiz=models.CharField(max_length=2,choices=op_manipulacion_lapiz,default='G1')
    sensibilidad_tacto=models.CharField(max_length=2,choices=op_sensi_tacto,default='H1')
    #CARACTERÍSTICAS DE SU LENGUAJE
    lenguaje_compresivo=models.CharField(max_length=2,choices=op_len_comprensivo,default='A1')
    lenguaje_expresivo=models.CharField(max_length=2,choices=op_len_expresivo,default='B1')
    def __str__(self):   
        return self.id