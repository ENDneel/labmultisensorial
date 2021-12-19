from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from Evaluacion.models import EvaluacionD, EvaluacionD1, EvaluacionD2, EvaluacionD3, EvaluacionD4, EvaluacionD5, EvaluacionD6, EvaluacionD7, EvaluacionD8, EvaluacionD9
from Recomendacion.models import RecomendacionD1, RecomendacionD2, RecomendacionD3, RecomendacionD4, RecomendacionD5, RecomendacionD6, RecomendacionD7, RecomendacionD8, RecomendacionD9, RecomendacionEst
from Seguimiento.models import RecomendacionD1S, RecomendacionD2S, RecomendacionD3S, RecomendacionD4S, RecomendacionD5S, RecomendacionD6S, RecomendacionD7S, RecomendacionD8S, RecomendacionD9S
from estudiante.models import Estudiante

# Create your views here.
class ModulosView(TemplateView):
    print("si entro aqui para los modulos")
    template_name = 'modulos/motricidad.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context

class StemView(TemplateView):

    template_name = 'modulos/stem.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context

class LapizDetailView(TemplateView):
    template_name = 'modulos/lapiz.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=EvaluacionD.Estudiante.id=self.kwargs['pk']
        est=Estudiante.objects.get(id=self.kwargs['pk'])
        print("wssssssssssssssssssssssssssssssss ",pk)

        evaluacionD1=validarEvaluacion(EvaluacionD1,pk) 
        evaluacionD2=validarEvaluacion(EvaluacionD2,pk)
        evaluacionD3=validarEvaluacion(EvaluacionD3,pk)
        evaluacionD4=validarEvaluacion(EvaluacionD4,pk)
        evaluacionD5=validarEvaluacion(EvaluacionD5,pk)
        evaluacionD6=validarEvaluacion(EvaluacionD5,pk)
        evaluacionD7=validarEvaluacion(EvaluacionD7,pk)
        evaluacionD8=validarEvaluacion(EvaluacionD8,pk)
        evaluacionD9=validarEvaluacion(EvaluacionD9,pk)
        idreco=RecomendacionEst.objects.filter(Estudiante__id=self.kwargs['pk']).order_by("id")
        recomendaciones={
            "reco1":valiadrRecomendacion(RecomendacionD1,idreco),
            "reco2":valiadrRecomendacion(RecomendacionD2,idreco),
            "reco3":valiadrRecomendacion(RecomendacionD3,idreco),
            "reco4":valiadrRecomendacion(RecomendacionD4,idreco),
            "reco5":valiadrRecomendacion(RecomendacionD5,idreco),
            "reco6":valiadrRecomendacion(RecomendacionD6,idreco),
            "reco7":valiadrRecomendacion(RecomendacionD7,idreco),
            "reco8":valiadrRecomendacion(RecomendacionD8,idreco),
            "reco9":valiadrRecomendacion(RecomendacionD9,idreco),

        }
        seguimientos={
            "reco1":valiadrSeguimiento(RecomendacionD1S,idreco),
            "reco2":valiadrSeguimiento(RecomendacionD2S,idreco),
            "reco3":valiadrSeguimiento(RecomendacionD3S,idreco),
            "reco4":valiadrSeguimiento(RecomendacionD4S,idreco),
            "reco5":valiadrSeguimiento(RecomendacionD5S,idreco),
            "reco6":valiadrSeguimiento(RecomendacionD6S,idreco),
            "reco7":valiadrSeguimiento(RecomendacionD7S,idreco),
            "reco8":valiadrSeguimiento(RecomendacionD8S,idreco),
            "reco9":valiadrSeguimiento(RecomendacionD9S,idreco),

        }
        context["Eval1"]=evaluacionD1
        context["Eval2"]=evaluacionD2
        context["Eval3"]=evaluacionD3
        context["Eval4"]=evaluacionD4
        context["Eval5"]=evaluacionD5
        context["Eval6"]=evaluacionD6
        context["Eval7"]=evaluacionD7
        context["Eval8"]=evaluacionD8
        context["Eval9"]=evaluacionD9
        context["recos"]=recomendaciones
        context["seg"]=seguimientos
        context["est"]=est
        print("si salio")

        return context

def validarEvaluacion(eval,id):
    try:
        result=eval.objects.get(EvaluacionD=id)
        return result
    except:
        return None
def valiadrRecomendacion(rec,idreco):
    try:
        result=rec.objects.get(RecomendacionEst_id=idreco[0].id)
        return result
    except:
        return None

def valiadrSeguimiento(seg,idreco):
    try:
        result=seg.objects.get(RecomendacionEst_id=idreco[0].id)
        return result
    except:
        return None


class CuboTemplateView(TemplateView):
    template_name = 'modulos/cubo.html'