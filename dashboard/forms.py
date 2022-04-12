# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from estudiante.models import Estudiante, Formulario

class EstudianteForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputNombre",
                "placeholder": "Nombre"
            }
        ))
    apellido = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputApellido",
                "placeholder": "apellido"
            }
        ))
    grado_Educacion = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputEsco", },
            choices=[
                ('No Escolarizado', 'No Escolarizado'),
                ('Educacion Inicial', 'Educacion Inicial'),
                ('Educacion Basica', 'Educacion Basica'),
            ]
        ))
    edad_Cronologica = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputEdadC",
                "placeholder": "Edad Cronologica"
            }
        ))
    edad_Mental = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputEdadM",
                "placeholder": "Edad Mental"
            }
        ))
    sexo = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputEsco", },
            choices=[
                ('Masculino', 'Masculino'),
                ('Femenino', 'Femenino'),
               
            ]
        ))

    class Meta:
        model = Estudiante
        fields = '__all__'


op_discapacidad_intelectual_auditiva = [('No presenta', 'No presenta'), ('Leve', 'Leve'), (
    'Moderado', 'Moderado'), ('Severo', 'Severo'), ('Profundo', 'Profundo')]
op_discapacidad_visual = [('No presenta', 'No presenta'), ('Leve', 'Leve'), (
    'Moderado', 'Moderado'), ('Severo', 'Severo'), ('Total', 'Total')]
op_discapacidad_motriz = [('No presenta', 'No presenta'),
                          ('Leve', 'Leve'), ('Moderado', 'Moderado'), ('Severo', 'Severo')]
op_discapacioda_pci = [('No presenta', 'No presenta'), ('Espástica', 'Espástica'),
                       ('Atetósica', 'Atetósica'), ('Atáxica', 'Atáxica'), ('Mixta', 'Mixta ')]
op_discapacidad_auditiva_prof = [
    ('No presenta', 'No presenta'), ('Unilateral', 'Unilateral'), ('Bilateral', 'Bilatera')]
op_discapacidad_pci_prof = [('No presenta', 'No presenta'), ('Monoplejía', 'Monoplejía'), ('Hemiplejía',
                                                                                           'Hemiplejía'), ('Paraplejía', 'Paraplejía'), ('Triplejía', 'Triplejía'), ('Tetraplejía', 'Tetraplejía')]
opcion = [('Si', 'Si'), ('No', 'No')]
op_control_cuerpo = [('A1', 'Mantiene el control total de su cuerpo'), ('A2', 'Mantiene el control de su cuerpo con dificultad en el equilibrio y le gustan las actividades de motricidad gruesa',),
                     ('A3', 'Mantiene el control de su cuerpo con dificultad en el equilibrio y no le gustan las actividades de motricidad gruesa'),
                     ('A4', 'Mantiene el control de su cuerpo, pero le cuesta realizar actividades de motricidad gruesa'), ('A5', 'No mantiene el control de su cuerpo, necesita apoyo y supervisión total')]
op_cord_oculo_manual = [('B1', 'Buena coordinación óculo manual'),
                        ('B2', 'Dificultad en mantener la coordinación óculo manual')]
op_atencion = [('C1', 'Mantiene la atención durante una tarea asignada'), ('C2', 'Mantiene la atención durante una tarea asignada a pesar que se demora, pero la culmina'),
               ('C3', 'La mayoría de las veces mantiene la atención en una tarea asignada'), ('C4',
                                                                                              'Le cuesta mantener la atención en una tarea asignada, se distrae con facilidad'),
               ('C5', 'Le cuesta mantener la atención en una tarea asignada, quiere terminarla rápido'), ('C6', 'Mantiene la atención por períodos cortos en objetos con luces y sonidos')]
op_lateralidad = [('D1', 'Definida'), ('D2', 'Cambia de mano constantemente al realizar una actividad'),
                  ('D3', 'Cambia de mano en pocas ocasiones, pero utiliza más una mano')]
op_diso_manos = [('E1', 'Utiliza constantemente la mano de apoyo'), ('E2',
                                                                     'Utiliza a veces la mano de apoyo'), ('E3', 'No utiliza la mano de apoyo')]
op_predis_tarea_mesa = [('F1', 'Permanece sentado durante una tarea'), (
    'F2', 'Le cuesta mantenerse sentado en una tarea'), ('F3', 'No permanece sentado')]
op_manipulacion_lapiz = [('G1', 'Le atraen los lápices y los manipula'), ('G2', 'Le atraen poco los lápices y los manipula poco'), ('G3', 'No le atraen los lápices ni los manipula'),
                         ('G4', 'No le atraen los lápices ni los manipula a menos de que sean necesarios en la tarea asignada')]
op_sensi_tacto = [('H1', 'Tolera actividades que implican ensuciarse y mojarse las manos'), ('H2', 'Tolera poco las actividades que implican ensuciarse o mojarse las manos'),
                  ('H3', 'No tolera actividades que implican ensuciarse o mojarse las manos')]
op_len_comprensivo = [('A1', 'Tiene buena comprensión'), ('A2', 'Su comprensión es buena, pero necesita de apoyos visuales y señas'), ('A3', 'Su comprensión es regular, hay que repetirle algunas veces la consigna'),
                      ('A4', 'Su comprensión es regular a pesar de repetirle verbalmente necesita de apoyos visuales.'), ('A5', 'Su comprensión es mala, responde por reflejos')]
op_len_expresivo = [('B1', 'Tiene buen lenguaje expresivo'), ('B2', 'Su lenguaje es claro, rígido, repetitivo y le cuesta participar en conversaciones'), ('B3', 'Se expresa mediante el lenguaje oral con una cierta distorsión en la entonación de la voz'),
                    ('B4', 'Se expresa mediante sonidos guturales, gritos y llanto'), ('B5', 'Se expresa mediante lenguaje oral, pero tiene dificultad en pronunciar claramente'), (
                        'B6', 'Se expresa mediante lenguaje oral con palabras monosílabas y bisílabas'),
                    ('B7', 'Se expresa mediante Sistemas Alternativos y Aumentativos de Comunicación (pictogramas)'), ('B8', 'Se expresa mediante lenguaje de señas y Sistemas Alternativos y Aumentativos de Comunicación')]


class FormularioForm(forms.ModelForm):
    disc_intelectual_grado = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputIntelectual", },
            choices=op_discapacidad_intelectual_auditiva
        ))
    disc_visual_grado = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputVisula", },
            choices=op_discapacidad_visual
        ))
    disc_motriz_grado = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputMotriz", },
            choices=op_discapacidad_motriz
        ))

    disc_auditiva_grado = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputAuditiva", },

            choices=op_discapacidad_intelectual_auditiva
        ))

    disc_auditiva_profundidad = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputAuditivaprof", },
            choices=op_discapacidad_auditiva_prof
        ))
    disc_pci_grado = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputPCI", },
            choices=op_discapacioda_pci
        ))

    disc_pci_profundidad = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputPCIProf", },
            choices=op_discapacidad_pci_prof
        ))
    sindrome_down = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
                # 'checked': "No"
            },
            choices=opcion
        )
    )
    sindrome_lennon = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
               # 'checked': "No"
            },
            choices=opcion
        )
    )
    sindrome_te = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
               # 'checked': "No"
            },
            choices=opcion
        )
    )
    sindorme_tdah = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
                #'checked': "No"
            },
            choices=opcion
        )
    )
    transtorno_agresivo = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
                #'checked': "No"
            },
            choices=opcion
        )
    )

    control_cuerpo = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_control_cuerpo
        )

    )
    cord_oculo_manual = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_cord_oculo_manual
        )

    )
    atencion = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_atencion
        )

    )
    lateralidad = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_lateralidad
        )

    )
    disociacion_manos = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_diso_manos
        )

    )
    predispo_mesa = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_predis_tarea_mesa
        )

    )
    manipulacion_lapiz = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_manipulacion_lapiz
        )

    )
    sensibilidad_tacto = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_sensi_tacto
        )

    )
    lenguaje_compresivo = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_len_comprensivo
        )

    )
    lenguaje_expresivo = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "input", },
            choices=op_len_expresivo
        )

    )

    class Meta:
        model = Formulario
        fields = ['disc_intelectual_grado', 'disc_visual_grado', 'disc_motriz_grado',
                  'disc_auditiva_grado', 'disc_auditiva_profundidad', 'disc_pci_grado', 'disc_pci_profundidad',
                  'sindrome_down', 'sindrome_lennon', 'sindrome_te', 'sindorme_tdah', 'transtorno_agresivo', 'control_cuerpo',
                  'cord_oculo_manual', 'atencion', 'lateralidad', 'disociacion_manos', 'predispo_mesa', 'manipulacion_lapiz',
                  'sensibilidad_tacto', 'lenguaje_compresivo', 'lenguaje_expresivo']


