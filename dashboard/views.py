from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from estudiante.models import Estudiante, Formulario
from sesion.models import Sesion,Tablero
from django.http import HttpResponse, request
from .forms import EstudianteForm, FormularioForm
from django.views.generic.detail import DetailView
from django.db.models import Count
import socket
# Create your views here.


class EstChartView(TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        ip=socket.gethostbyname(socket.gethostname())
        if ip =="172.16.42.56":
            sinc="True"
        else:
            sinc="False"
        context['ip'] = sinc
        return context

    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['est'] = Estudiante.objects.all()
    #     return context


def ListEstudent(request):
    dir = ''
    print("........", request.POST)
    data = {
        'form': EstudianteForm,
        'form2': FormularioForm,

    }
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        form2 = FormularioForm(request.POST)
        if form.is_valid() and form2.is_valid():

            solicitud = form2.save(commit=False)
            solicitud.Estudiante = form.save()
            solicitud.save()
            dir = 'dashboard'
            return redirect(dir)

        else:
            print(form.errors)
            print(form2.errors)
    else:

        print("hubo un error")
    return render(request, 'dashboard/formularioEst.html', data)


class EstudentDetail(DetailView):

    model = Formulario
    #template_name = 'dashboard/infoAlumno.html'
    print("aqui")

    def get_object(self, queryset=None):
        return Formulario.objects.get(Estudiante__id=self.kwargs.get('pk'))


class GraficEstudent(TemplateView):
    template_name = 'dashboard/GraphEstu.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
       
        context['qs'] = Estudiante.objects.all()
       
        pknombre=self.kwargs.get('nombre')
        if pknombre!='null':
            motg= len(Sesion.objects.filter(Estudiante__nombre=pknombre.split(' ')[0]).filter(Estudiante__apellido=pknombre.split(' ')[1]).filter(area="Motricidad Gruesa"))
            prees= len(Sesion.objects.filter(Estudiante__nombre=pknombre.split(' ')[0]).filter(Estudiante__apellido=pknombre.split(' ')[1]).filter(area="Preescritura"))
            esc=len(Sesion.objects.filter(Estudiante__nombre=pknombre.split(' ')[0]).filter(Estudiante__apellido=pknombre.split(' ')[1]).filter(area="Escritura"))
            data_sesion=[esc, prees, motg, 5]
            context['labdata']=data_sesion        
        else:
            context['valid']="True"
            context['alldata']=Sesion.objects.all().values('fecha').order_by('fecha').annotate(fecha_coutn=Count('fecha'))

            # for i in fechas:
            #     print(i['fecha_coutn']," ddddddd ",i['fecha'])
        return context