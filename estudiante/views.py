import estudiante
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Estudiante, Formulario
from dashboard.forms import FormularioForm
from django.views.generic.list import ListView
from django.views.generic import TemplateView

# Create your views here.
def EstudentDetail(request,pk):
    estudiante=Formulario.objects.all()
    indice=['Mantiene el control total de su cuerpo','Mantiene el control de su cuerpo con dificultad en el equilibrio y le gustan las actividades de motricidad gruesa',
    'Mantiene el control de su cuerpo con dificultad en el equilibrio y no le gustan las actividades de motricidad gruesa','Mantiene el control de su cuerpo, pero le cuesta realizar actividades de motricidad gruesa.',
    'No mantiene el control de su cuerpo, necesita apoyo y supervisión total.','Buena coordinación óculo manual','Dificultad en mantener la coordinación óculo manual',
    'Mantiene la atención durante una tarea asignada','Mantiene la atención durante una tarea asignada a pesar que se demora, pero la culmina','La mayoría de las veces mantiene la atención en una tarea asignada',
    'Le cuesta mantener la atención en una tarea asignada, se distrae con facilidad','Le cuesta mantener la atención en una tarea asignada, quiere terminarla rápido','Mantiene la atención por períodos cortos en objetos con luces y sonidos',
    'Definida','Cambia de mano constantemente al realizar una actividad','Cambia de mano en pocas ocasiones, pero utiliza más una mano','Utiliza constantemente la mano de apoyo','Utiliza a veces la mano de apoyo',
    'No utiliza la mano de apoyo','Permanece sentado durante una tarea','Le cuesta mantenerse sentado en una tarea','No permanece sentado','Le atraen los lápices y los manipula',
    'Le atraen poco los lápices y los manipula poco','No le atraen los lápices ni los manipula','No le atraen los lápices ni los manipula a menos de que sean necesarios en la tarea asignada',
    'Tolera actividades que implican ensuciarse y mojarse las manos','Tolera poco las actividades que implican ensuciarse o mojarse las manos','No tolera actividades que implican ensuciarse o mojarse las manos',
    'Tiene buena comprensión','Su comprensión es buena, pero necesita de apoyos visuales y señas','Su comprensión es regular, hay que repetirle algunas veces la consigna','Su comprensión es regular a pesar de repetirle verbalmente necesita de apoyos visuales.',
    'Su comprensión es mala, responde por reflejos','Tiene buen lenguaje expresivo','Su lenguaje es claro, rígido, repetitivo y le cuesta participar en conversaciones','Se expresa mediante el lenguaje oral con una cierta distorsión en la entonación de la voz',
    'Se expresa mediante sonidos guturales, gritos y llanto','Se expresa mediante lenguaje oral, pero tiene dificultad en pronunciar claramente','Se expresa mediante lenguaje oral con palabras monosílabas y bisílabas',
    'Se expresa mediante Sistemas Alternativos y Aumentativos de Comunicación (pictogramas)','Se expresa mediante lenguaje de señas y Sistemas Alternativos y Aumentativos de Comunicación']
    for i in estudiante:
        if i.Estudiante.id==pk:
            print(i.Estudiante.nombre)
            contexto = {'est': i,'indice':indice}
    return render(request, 'estudiante/formulario_detail.html',contexto)


class EstudenUpdateView(UpdateView):
    # specify the model you want to use
    model = Formulario
    form_class = FormularioForm 
    success_url='/dashboard/'


class EstudentListView(ListView):
    model = Estudiante
    paginate_by = 100  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['est'] = Estudiante.objects.all()
        return context