from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from estudiante.models import Estudiante, Formulario
from django.http import HttpResponse, request
from .forms import EstudianteForm,FormularioForm
from django.views.generic.detail import DetailView
# Create your views here.
class EstChartView(TemplateView):
    template_name = 'dashboard/index.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['est'] = Estudiante.objects.all()
    #     return context

def ListEstudent(request):
    dir=''
    print("........",request.POST)
    data = {
        'form': EstudianteForm,
        'form2': FormularioForm,

    }
    if request.method == "POST" :
        form = EstudianteForm(request.POST)
        form2=FormularioForm(request.POST)
        if form.is_valid() and form2.is_valid():

            solicitud = form2.save(commit=False)
            solicitud.Estudiante = form.save()
            solicitud.save()
            dir='dashboard'
            return redirect(dir)
           
        else:
            print(form.errors)
            print(form2.errors)
    else:
        
        print("hubo un error")
    return render(request,'dashboard/formularioEst.html', data)

class EstudentDetail(DetailView):

    model = Formulario
    #template_name = 'dashboard/infoAlumno.html'
    print("aqui")
    def get_object(self, queryset=None):
        return Formulario.objects.get(Estudiante__id=self.kwargs.get('pk'))



          
    