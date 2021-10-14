import sesion
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Sesion, Tablero
import socket
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

class TableroCView(TemplateView):
    template_name = 'sesion/tableroC.html'


def createSesionTablero(request,pk):
    print(pk)
    ip=socket.gethostbyname(socket.gethostname())
    if ip =="172.16.42.56":
        sesiones=Sesion.objects.filter(serial__contains='Serv').last()
    else:
        sesiones=Sesion.objects.filter(serial__contains='PiA').last()

    
    print(sesiones)
    serieL=""
    serieN=""
   
    for i in sesiones.serial:
        if i.isdigit():
            serieN+=i
        else:
            serieL+=i
    print(serieL," ********* ",serieN)
    sigSerie=serieL+str(int(serieN)+1)
    print(sigSerie)

    # "b":(int(sigSerie)+1)
    return render(request,'sesion/tablero.html',{"a":pk,"b":sigSerie})

def createSesionTableroC(request,pk):
    return render(request,'sesion/tableroC.html',{"a":pk})
