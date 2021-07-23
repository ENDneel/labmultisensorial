from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EvaluacionD, EvaluacionD1, EvaluacionD2, EvaluacionD3, EvaluacionD4, EvaluacionD5, EvaluacionD6, EvaluacionD7, EvaluacionD8, EvaluacionD9
from .serializer import EvaluacionDSerializer, EvaluacionD1Serializer, EvaluacionD2Serializer, EvaluacionD3Serializer, EvaluacionD4Serializer, EvaluacionD5Serializer, EvaluacionD6Serializer, EvaluacionD7Serializer, EvaluacionD8Serializer, EvaluacionD9Serializer
from Recomendacion.models import RecomendacionEst, RecomendacionD1, RecomendacionD2, RecomendacionD3, RecomendacionD4, RecomendacionD5, RecomendacionD6, RecomendacionD7, RecomendacionD8, RecomendacionD9
from estudiante.models import Estudiante
from Seguimiento.models import *
from clips import Environment, Symbol
import clips
from rest_framework.permissions import IsAuthenticated,AllowAny

@api_view(['POST'])
def EvaluacionD_Post(request):
    authentication_classes = [AllowAny]
    if request.method  == 'POST':
        serializer = EvaluacionDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            recomendacion_(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_(Eval):
    Est=Estudiante.objects.get(id=Eval['Estudiante'])
    recoEs = RecomendacionEst(
        Estudiante = Est
    )
    recoEs.save()

@api_view(['POST'])
def EvaluacionD1_Post(request):
    authentication_classes = [AllowAny]
    if request.method  == 'POST':
        serializerD1 = EvaluacionD1Serializer(data=request.data)
        if serializerD1.is_valid():
            serializerD1.save()
            recomendacion_D1(serializerD1.data)
            return Response(serializerD1.data, status=status.HTTP_201_CREATED)
        return Response(serializerD1.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D1(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    #------ Recommendation D1 ---------------------------------------
    D1  =  Eval['D1']
    if D1 == "Logrado": val=2
    if D1 == "En vias de logro": val=1
    if D1 == "No logrado": val=0
    sAuxF = "(assert  (D1 "+ str(val) +"))"
    clp.eval(sAuxF)
    
    D12  =  Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =  Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)

    clp.run()

    evaluar1 = "(find-all-facts ((?x recommendationD1 )) TRUE)"
    value1  =  clp.eval(evaluar1)

    if(len(value1)>0):
        valF=dict(value1[0])
        Fs = valF.get("Frecuencia_Semanal")
        AC1 = valF.get("AC1")
        AC2 = valF.get("AC2")
        AC3 = valF.get("AC3")
        AC4 = valF.get("AC4")
        AC5 = valF.get("AC5")
        AC41 = valF.get("AC41")
        AC42 = valF.get("AC42")
        Se = valF.get("Semanas")

        try:
            reco = RecomendacionD1.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC1    =   AC1
            reco.AC2    =   AC2
            reco.AC3    =   AC3
            reco.AC4    =   AC4
            reco.AC5    =   AC5
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()

            recoS = RecomendacionD1S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC1    =   AC1
            recoS.AC2    =   AC2
            recoS.AC3    =   AC3
            recoS.AC4    =   AC4
            recoS.AC5    =   AC5
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD1.DoesNotExist:
            r = RecomendacionD1(
                RecomendacionEst  =   recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC1    =   AC1,
                AC2    =   AC2,
                AC3    =   AC3,
                AC4    =   AC4,
                AC5    =   AC5,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rs = RecomendacionD1S(
                RecomendacionEst  =   recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC1    =   AC1,
                AC2    =   AC2,
                AC3    =   AC3,
                AC4    =   AC4,
                AC5    =   AC5,
                AC41   =   AC41,
                AC42   =   AC42)
            rs.save()
            pass


        except RecomendacionD1.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass

    clp.reset()

#-----------------recomendacion D2
@api_view(['POST'])
def EvaluacionD2_Post(request):
    if request.method  == 'POST':
        serializerD2 = EvaluacionD2Serializer(data=request.data)
        if serializerD2.is_valid():
            serializerD2.save()
            recomendacion_D2(serializerD2.data)
            return Response(serializerD2.data, status=status.HTTP_201_CREATED)
        return Response(serializerD2.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D2(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')

    D2  =  Eval['D2']
    if D2 == "Logrado": val=2
    if D2 == "En vias de logro": val=1
    if D2 == "No logrado": val=0
    sAuxF = "(assert  (D2 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =  Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =  Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)

    clp.run()

    evaluar2 = "(find-all-facts ((?x recommendationD2 )) TRUE)"
    value2  =  clp.eval(evaluar2)
    print(value2)
    if(len(value2)>0):
        val2=dict(value2[0])
        Fs = val2.get("Frecuencia_Semanal")
        AC6 = val2.get("AC6")
        AC7 = val2.get("AC7")
        AC8 = val2.get("AC8")
        AC9 = val2.get("AC9")
        AC10 = val2.get("AC10")
        AC41 = val2.get("AC41")
        AC42 = val2.get("AC42")
        Se = val2.get("Semanas")

        try:
            reco = RecomendacionD2.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC6    =   AC6
            reco.AC7    =   AC7
            reco.AC8    =   AC8
            reco.AC9    =   AC9
            reco.AC10    =   AC10
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()
            recoS = RecomendacionD2S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC6    =   AC6
            recoS.AC7    =   AC7
            recoS.AC8    =   AC8
            recoS.AC9    =   AC9
            recoS.AC10    =   AC10
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()
        except RecomendacionD2.DoesNotExist:
            print('aquiCreaC')
            r = RecomendacionD2(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10    =   AC10,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rs = RecomendacionD2S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10    =   AC10,
                AC41   =   AC41,
                AC42   =   AC42)
            rs.save()
            

        except RecomendacionD1.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    clp.reset()
#-----------------recomendacion D3
@api_view(['POST'])
def EvaluacionD3_Post(request):
    if request.method  == 'POST':
        serializerD3 = EvaluacionD3Serializer(data=request.data)
        if serializerD3.is_valid():
            serializerD3.save()
            recomendacion_D3(serializerD3.data)
            return Response(serializerD3.data, status=status.HTTP_201_CREATED)
        return Response(serializerD3.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D3(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')

    D3  =  Eval['D3']
    if D3 == "Logrado": val=2
    if D3 == "En vias de logro": val=1
    if D3 == "No logrado": val=0
    sAuxF = "(assert  (D3 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =  Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =  Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)

    clp.run()

    evaluar3 = "(find-all-facts ((?x recommendationD3 )) TRUE)"
    value3  =  clp.eval(evaluar3)
    if(len(value3)>0):
        val3=dict(value3[0])
        Fs = val3.get("Frecuencia_Semanal")
        AC11 = val3.get("AC11")
        AC12 = val3.get("AC12")
        AC13 = val3.get("AC13")
        AC14 = val3.get("AC14")
        AC15 = val3.get("AC15")
        AC41 = val3.get("AC41")
        AC42 = val3.get("AC42")
        Se = val3.get("Semanas")

        try:
            reco3 = RecomendacionD3.objects.get(RecomendacionEst=recoEs.id)
            reco3.FrecuenciaS=   Fs
            reco3.Semanas    =   Se
            reco3.AC11    =   AC11
            reco3.AC12    =   AC12
            reco3.AC13    =   AC13
            reco3.AC14    =   AC14
            reco3.AC15    =   AC15
            reco3.AC41   =   AC41
            reco3.AC42   =   AC42
            reco3.save()

            recoS = RecomendacionD3S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC11    =   AC11
            recoS.AC12    =   AC12
            recoS.AC13    =   AC13
            recoS.AC14    =   AC14
            recoS.AC15    =   AC15
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD3.DoesNotExist:
            r = RecomendacionD3(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC11    =   AC11,
                AC12    =   AC12,
                AC13    =   AC13,
                AC14    =   AC14,
                AC15    =   AC15,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rs = RecomendacionD3S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC11    =   AC11,
                AC12    =   AC12,
                AC13    =   AC13,
                AC14    =   AC14,
                AC15    =   AC15,
                AC41   =   AC41,
                AC42   =   AC42)
            rs.save()
            pass
        except RecomendacionD3.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass

    clp.reset()
@api_view(['POST'])
def EvaluacionD4_Post(request):
    if request.method  == 'POST':
        serializerD4 = EvaluacionD4Serializer(data=request.data)
        if serializerD4.is_valid():
            serializerD4.save()
            recomendacion_D4(serializerD4.data)
            return Response(serializerD4.data, status=status.HTTP_201_CREATED)
        return Response(serializerD4.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D4(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    #------ Recommendation D1 ---------------------------------------
    D4  =  Eval['D4']
    
    if D4 == "Logrado": val=2
    if D4 == "En vias de logro": val=1
    if D4 == "No logrado": val=0
    sAuxF = "(assert  (D4 "+ str(val) +"))"
    clp.eval(sAuxF)

    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
    clp.eval(sAuxF)

    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)

    clp.run()

    evaluar4 = "(find-all-facts ((?x recommendationD4 )) TRUE)"
    value4  =  clp.eval(evaluar4)
    if(len(value4)>0):
        val4=dict(value4[0])
        Fs = val4.get("Frecuencia_Semanal")
        AC16 = val4.get("AC16")
        AC17 = val4.get("AC17")
        AC18 = val4.get("AC18")
        AC19 = val4.get("AC19")
        AC20 = val4.get("AC20")
        AC39 = val4.get("AC39")
        AC40 = val4.get("AC40")
        AC41 = val4.get("AC41")
        AC42 = val4.get("AC42")
        Se = val4.get("Semanas")

        try:
            reco = RecomendacionD4.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC16    =   AC16
            reco.AC17    =   AC17
            reco.AC18    =   AC18
            reco.AC19    =   AC19
            reco.AC20    =   AC20
            reco.AC39    =   AC39
            reco.AC40   =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()

            recoS = RecomendacionD4S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC16    =   AC16
            recoS.AC17    =   AC17
            recoS.AC18    =   AC18
            recoS.AC19    =   AC19
            recoS.AC20    =   AC20
            recoS.AC39    =   AC39
            recoS.AC40   =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD4.DoesNotExist:
            r = RecomendacionD4(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC16    =   AC16,
                AC17    =   AC17,
                AC18   =   AC18,
                AC19    =   AC19,
                AC20    =   AC20,
                AC39    =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rs = RecomendacionD4S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC16    =   AC16,
                AC17    =   AC17,
                AC18   =   AC18,
                AC19    =   AC19,
                AC20    =   AC20,
                AC39    =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            rs.save()
            pass
        except RecomendacionD1.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    clp.reset()

    #-----------recomendacion post D4
@api_view(['POST'])
def EvaluacionD5_Post(request):
    if request.method  == 'POST':
        serializerD5 = EvaluacionD5Serializer(data=request.data)
        if serializerD5.is_valid():
            serializerD5.save()
            recomendacion_D5(serializerD5.data)
            return Response(serializerD5.data, status=status.HTTP_201_CREATED)
        return Response(serializerD5.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D5(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    D5  =  Eval['D5']
    
    if D5 == "Logrado": val=2
    if D5 == "En vias de logro": val=1
    if D5 == "No logrado": val=0
    sAuxF = "(assert  (D5 "+ str(val) +"))"
    clp.eval(sAuxF)

    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
    clp.eval(sAuxF)

    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)
    clp.run()
    evaluar5 = "(find-all-facts ((?x recommendationD5 )) TRUE)"
    value5  =  clp.eval(evaluar5)
    if(len(value5)>0):
        val5=dict(value5[0])
        Fs = val5.get("Frecuencia_Semanal")
        AC21 = val5.get("AC21")
        AC22 = val5.get("AC22")
        AC23 = val5.get("AC23")
        AC24 = val5.get("AC24")
        AC39 = val5.get("AC39")
        AC40 = val5.get("AC40")
        AC41 = val5.get("AC41")
        AC42 = val5.get("AC42")
        Se = val5.get("Semanas")

        try:
            reco = RecomendacionD5.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC21    =   AC21
            reco.AC22    =   AC22
            reco.AC23    =   AC23
            reco.AC24    =   AC24
            reco.AC39    =   AC39
            reco.AC40   =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()

            recoS = RecomendacionD5S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC21    =   AC21
            recoS.AC22    =   AC22
            recoS.AC23    =   AC23
            recoS.AC24    =   AC24
            recoS.AC39    =   AC39
            recoS.AC40   =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD5.DoesNotExist:
            r = RecomendacionD5(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC21    =   AC21,
                AC22    =   AC22,
                AC23    =   AC23,
                AC24    =   AC24,
                AC39    =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rS = RecomendacionD5S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC21    =   AC21,
                AC22    =   AC22,
                AC23    =   AC23,
                AC24    =   AC24,
                AC39    =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            rS.save()
            pass

        except RecomendacionD5.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    clp.reset()

  #-----------recomendacion post D6
@api_view(['POST'])
def EvaluacionD6_Post(request):
    if request.method  == 'POST':
        serializerD6 = EvaluacionD6Serializer(data=request.data)
        if serializerD6.is_valid():
            serializerD6.save()
            recomendacion_D6(serializerD6.data)
            return Response(serializerD6.data, status=status.HTTP_201_CREATED)
        return Response(serializerD6.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D6(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    D6  =  Eval['D6']
    if D6 == "Logrado": val=2
    if D6 == "En vias de logro": val=1
    if D6 == "No logrado": val=0
    sAuxF = "(assert  (D6 "+ str(val) +"))"
    clp.eval(sAuxF)
    #print(sAuxF)
    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
    clp.eval(sAuxF)
    #print(sAuxF)
    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)
    clp.run()

    evaluar6 = "(find-all-facts ((?x recommendationD6 )) TRUE)"
    value6  =  clp.eval(evaluar6)
    #print('eval6')
    print(value6)
    if(len(value6)>0):
        val6=dict(value6[0])
        Fs = val6.get("Frecuencia_Semanal")
        AC25 = val6.get("AC25")
        AC26 = val6.get("AC26")
        AC27 = val6.get("AC27")
        AC28 = val6.get("AC28")
        AC39 = val6.get("AC39")
        AC40 = val6.get("AC40")
        AC41 = val6.get("AC41")
        AC42 = val6.get("AC42")
        Se = val6.get("Semanas")

        try:
            reco = RecomendacionD6.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC25    =   AC25
            reco.AC26    =   AC26
            reco.AC27    =   AC27
            reco.AC28    =   AC28
            reco.AC39   =   AC39
            reco.AC40   =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()
           
            recoS = RecomendacionD6S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC25    =   AC25
            recoS.AC26    =   AC26
            recoS.AC27    =   AC27
            recoS.AC28    =   AC28
            recoS.AC39   =   AC39
            recoS.AC40   =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD6.DoesNotExist:
            r = RecomendacionD6(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC25   =   AC25,
                AC26    =   AC26,
                AC27    =   AC27,
                AC28    =   AC28,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            r.save()
            rs = RecomendacionD6S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC25   =   AC25,
                AC26    =   AC26,
                AC27    =   AC27,
                AC28    =   AC28,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42)
            rs.save()
            pass
   

        except RecomendacionD6.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    clp.reset()
 #-----------recomendacion post D7
@api_view(['POST'])
def EvaluacionD7_Post(request):
    if request.method  == 'POST':
        serializerD7 = EvaluacionD7Serializer(data=request.data)
        if serializerD7.is_valid():
            serializerD7.save()
            recomendacion_D7(serializerD7.data)
            return Response(serializerD7.data, status=status.HTTP_201_CREATED)
        return Response(serializerD7.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D7(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)

    clp = Environment()
    clp.load('SE.clp')
    #print(clp)
    D7  =  Eval['D7']
    if D7 == "Logrado": val=2
    if D7 == "En vias de logro": val=1
    if D7 == "No logrado": val=0
    sAuxF = "(assert  (D7 "+ str(val) +"))"
    #print(sAuxF)
    clp.eval(sAuxF)

    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
   #print(clp)
    clp.eval(sAuxF)
   
    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
  #print(clp)
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
   # print(sAuxF)
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    #print(sAuxF)
    clp.eval(sAuxF)

    D14  =  Eval['D14']
    if D14 == "Pronacion supinacion": val=1
    if D14 == "Movimiento Palmar": val=0
    sAuxF = "(assert  (D14 "+ str(val) +"))"
    #print(sAuxF)
    clp.eval(sAuxF)

    clp.run()

    evaluar7 = "(find-all-facts ((?x recommendationD7 )) TRUE)"
    value7  =  clp.eval(evaluar7)
    #print(value7)
    if(len(value7)>0):
        val7=dict(value7[0])
        Fs = val7.get("Frecuencia_Semanal")
        AC29 = val7.get("AC29")
        AC30 = val7.get("AC30")
        AC31 = val7.get("AC31")
        AC32 = val7.get("AC32")
        AC39 = val7.get("AC39")
        AC40 = val7.get("AC40")
        AC41 = val7.get("AC41")
        AC42 = val7.get("AC42")
        Se = val7.get("Semanas")

        try:
            reco = RecomendacionD7.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC29    =   AC29
            reco.AC30   =   AC30
            reco.AC31    =   AC31
            reco.AC32    =   AC32
            reco.AC39    =   AC39
            reco.AC40   =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()

            recoS = RecomendacionD7S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC29    =   AC29
            recoS.AC30   =   AC30
            recoS.AC31    =   AC31
            recoS.AC32    =   AC32
            recoS.AC39    =   AC39
            recoS.AC40   =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD7.DoesNotExist:
            r = RecomendacionD7(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC29    =   AC29,
                AC30    =   AC30,
                AC31    =   AC31,
                AC32    =   AC32,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                )
            r.save()
            rs= RecomendacionD7S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC29    =   AC29,
                AC30    =   AC30,
                AC31    =   AC31,
                AC32    =   AC32,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                )
            rs.save()
            pass
        except RecomendacionD7.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    clp.reset()

#-----------recomendacion post D8
@api_view(['POST'])
def EvaluacionD8_Post(request):
    if request.method  == 'POST':
        serializerD8 = EvaluacionD8Serializer(data=request.data)
        if serializerD8.is_valid():
            serializerD8.save()
            recomendacion_D8(serializerD8.data)
            return Response(serializerD8.data, status=status.HTTP_201_CREATED)
        return Response(serializerD8.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D8(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    D8  =  Eval['D8']
    if D8 == "Logrado": val=2
    if D8 == "En vias de logro": val=1
    if D8 == "No logrado": val=0
    sAuxF = "(assert  (D8 "+ str(val) +"))"
    clp.eval(sAuxF)

    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
    clp.eval(sAuxF)

    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)
    D14  =  Eval['D14']
    if D14 == "Pronacion supinacion": val=1
    if D14 == "Movimiento Palmar": val=0
    sAuxF = "(assert  (D14 "+ str(val) +"))"
    clp.eval(sAuxF)

    clp.run()
    evaluar8 = "(find-all-facts ((?x recommendationD8 )) TRUE)"
    value8  =  clp.eval(evaluar8)
    if(len(value8)>0):
        val8=dict(value8[0])
        Fs = val8.get("Frecuencia_Semanal")
        AC1 = val8.get("AC1")
        AC2 = val8.get("AC2")
        AC3 = val8.get("AC3")
        AC4 = val8.get("AC4")
        AC5 = val8.get("AC5")
        AC6 = val8.get("AC6")
        AC7 = val8.get("AC7")
        AC8 = val8.get("AC8")
        AC9 = val8.get("AC9")
        AC10 = val8.get("AC10")
        AC39 = val8.get("AC39")
        AC40 = val8.get("AC40")
        AC41 = val8.get("AC41")
        AC42 = val8.get("AC42")
        Se = val8.get("Semanas")

        try:
            reco = RecomendacionD8.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC1    =   AC1
            reco.AC2    =   AC2
            reco.AC3    =   AC3
            reco.AC4    =   AC4
            reco.AC5    =   AC5
            reco.AC6   =   AC6
            reco.AC7    =   AC7
            reco.AC8    =   AC8
            reco.AC9    =   AC9
            reco.AC10    =   AC10
            reco.AC39   =   AC39
            reco.AC40   =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.save()

            recoS = RecomendacionD8S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC1    =   AC1
            recoS.AC2    =   AC2
            recoS.AC3    =   AC3
            recoS.AC4    =   AC4
            recoS.AC5    =   AC5
            recoS.AC6   =   AC6
            recoS.AC7    =   AC7
            recoS.AC8    =   AC8
            recoS.AC9    =   AC9
            recoS.AC10    =   AC10
            recoS.AC39   =   AC39
            recoS.AC40   =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.save()

        except RecomendacionD8.DoesNotExist:
            r = RecomendacionD8(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC1    =   AC1,
                AC2    =   AC2,
                AC3    =   AC3,
                AC4    =   AC4,
                AC5    =   AC5,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10   =   AC10,
                AC39   =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                )
            r.save()
            rs = RecomendacionD8S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC1    =   AC1,
                AC2    =   AC2,
                AC3    =   AC3,
                AC4    =   AC4,
                AC5    =   AC5,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10   =   AC10,
                AC39   =   AC39,
                AC40   =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                )
            rs.save()
            pass

        except RecomendacionD8.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass
    
    clp.reset()

#-----------recomendacion post D9
@api_view(['POST'])
def EvaluacionD9_Post(request):
    if request.method  == 'POST':
        serializerD9 = EvaluacionD9Serializer(data=request.data)
        if serializerD9.is_valid():
            serializerD9.save()
            recomendacion_D9(serializerD9.data)
            return Response(serializerD9.data, status=status.HTTP_201_CREATED)
        return Response(serializerD9.errors, status=status.HTTP_400_BAD_REQUEST)

def recomendacion_D9(Eval):
    idEval = Eval['EvaluacionD']
    Eval_Est=EvaluacionD.objects.get(id=idEval)
    idEvalEst=Estudiante.objects.get(id=Eval_Est.Estudiante.id)
    recoEs = RecomendacionEst.objects.get(Estudiante=idEvalEst.id)
    clp = Environment()
    clp.load('SE.clp')
    D9  =  Eval['D9']
    if D9 == "Logrado": val=2
    if D9 == "En vias de logro": val=1
    if D9 == "No logrado": val=0
    sAuxF = "(assert  (D9 "+ str(val) +"))"
    clp.eval(sAuxF)

    D10  =   Eval['D10']
    if D10 == "Normal": val=2
    if D10 == "Hipertónico": val=1
    if D10 == "Hipotónico": val=0
    sAuxF = "(assert  (D10 "+ str(val) +"))"
    clp.eval(sAuxF)

    D11  =   Eval['D11']
    if D11 == "Tridigital": val=2
    if D11 == "Digital": val=1
    if D11 == "Modal": val=0
    sAuxF = "(assert  (D11 "+ str(val) +"))"
    clp.eval(sAuxF)

    D12  =   Eval['D12']
    if D12 == "Buena": val=1
    if D12 == "Mala": val=0
    sAuxF = "(assert  (D12 "+ str(val) +"))"
    clp.eval(sAuxF)

    D13  =   Eval['D13']
    if D13 == "No estresado": val=1
    if D13 == "Estresado": val=0
    sAuxF = "(assert  (D13 "+ str(val) +"))"
    clp.eval(sAuxF)
    D14  =  Eval['D14']
    if D14 == "Pronacion supinacion": val=1
    if D14 == "Movimiento Palmar": val=0
    sAuxF = "(assert  (D14 "+ str(val) +"))"
    clp.eval(sAuxF)
    clp.run()
    evaluar9 = "(find-all-facts ((?x recommendationD9 )) TRUE)"
    value9  =  clp.eval(evaluar9)
    if(len(value9)>0):
        val9=dict(value9[0])
        Fs = val9.get("Frecuencia_Semanal")
        AC6 = val9.get("AC6")
        AC7 = val9.get("AC7")
        AC8 = val9.get("AC8")
        AC9 = val9.get("AC9")
        AC10 = val9.get("AC10")
        AC34 = val9.get("AC34")
        AC35 = val9.get("AC35")
        AC36 = val9.get("AC36")
        AC37 = val9.get("AC37")
        AC38 = val9.get("AC38")
        AC39 = val9.get("AC39")
        AC40 = val9.get("AC40")
        AC41 = val9.get("AC41")
        AC42 = val9.get("AC42")
        AC43 = val9.get("AC43")
        Se = val9.get("Semanas")

        try:
            reco = RecomendacionD9.objects.get(RecomendacionEst=recoEs.id)
            reco.FrecuenciaS=   Fs
            reco.Semanas    =   Se
            reco.AC6    =   AC6
            reco.AC7    =   AC7
            reco.AC8    =   AC8
            reco.AC9    =   AC9
            reco.AC10    =   AC10
            reco.AC34   =   AC34
            reco.AC35   =   AC35
            reco.AC36    =   AC36
            reco.AC37    =   AC37
            reco.AC38    =   AC38
            reco.AC39    =   AC39
            reco.AC40    =   AC40
            reco.AC41   =   AC41
            reco.AC42   =   AC42
            reco.AC43   =   AC43
            reco.save()

            recoS = RecomendacionD9S.objects.get(RecomendacionEst=recoEs.id)
            recoS.FrecuenciaS=   Fs
            recoS.Semanas    =   Se
            recoS.AC6    =   AC6
            recoS.AC7    =   AC7
            recoS.AC8    =   AC8
            recoS.AC9    =   AC9
            recoS.AC10    =   AC10
            recoS.AC34   =   AC34
            recoS.AC35   =   AC35
            recoS.AC36    =   AC36
            recoS.AC37    =   AC37
            recoS.AC38    =   AC38
            recoS.AC39    =   AC39
            recoS.AC40    =   AC40
            recoS.AC41   =   AC41
            recoS.AC42   =   AC42
            recoS.AC43   =   AC43
            recoS.save()

        except RecomendacionD9.DoesNotExist:
            r = RecomendacionD9(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10    =   AC10,
                AC34   =   AC34,
                AC35   =   AC35,
                AC36    =   AC36,
                AC37    =   AC37,
                AC38    =   AC38,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                AC43   =   AC43,
                )
            r.save()
            rs = RecomendacionD9S(
                RecomendacionEst  =  recoEs,
                FrecuenciaS=   Fs,
                Semanas    =   Se,
                AC6    =   AC6,
                AC7    =   AC7,
                AC8    =   AC8,
                AC9    =   AC9,
                AC10    =   AC10,
                AC34   =   AC34,
                AC35   =   AC35,
                AC36    =   AC36,
                AC37    =   AC37,
                AC38    =   AC38,
                AC39    =   AC39,
                AC40    =   AC40,
                AC41   =   AC41,
                AC42   =   AC42,
                AC43   =   AC43,
                )
            rs.save()
            pass
        except RecomendacionD9.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass

    clp.reset()