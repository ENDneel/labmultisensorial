import sesion
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Sesion, Tablero
# Create your views here.


class SesionTableroDetail(DetailView):
    model = Tablero
    #template_name = 'dashboard/infoAlumno.html'

    def get_object(self, queryset=None):
        lista = []
        dic = {}
        tab = Tablero.objects.filter(
            Sesion__Estudiante__id=self.kwargs.get('pk'))
        sesi = Sesion.objects.filter(Estudiante__id=self.kwargs.get('pk'))
        id=self.kwargs.get('pk')
        print(id)
        # print(type(sesi))
        # for i in sesi:
        #     listaAc = []
        #     for j in tab:
        #         dic['sesion'] = i.id
        #         if i.id == j.Sesion.id:
        #             dic['actividades'] = {'actividad': j.Actividad}
        #             lista.append(dic)
        #     lista.append(dic)
        # print(len(lista))
        # print(lista)
        return sesi,tab,id


class TableroView(TemplateView):
    template_name = 'sesion/tablero.html'


def createSesion(request,pk):
    print(pk)

    return render(request,'sesion/tablero.html',{"a":pk})
