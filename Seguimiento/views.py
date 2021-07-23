from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
from Recomendacion.models import *
from Evaluacion.models import *
from django.http import HttpResponse
import pandas as pd
import io
from django.shortcuts import render
import xlsxwriter
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.


def index(request):
    resp = HttpResponse(content_type='application/xls')
    resp['Content-Disposition'] = 'attachment; filename=datos.xls'
    estud = Estudiante.objects.all()
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    row = 0
    col = 0

    estud = Estudiante.objects.all()
    datos = EvaluacionD1.objects.order_by("id")
    for est in estud:
        contador = 0
        hoja = est.nombre+est.apellido
        worksheet = workbook.add_worksheet(name=hoja)
        edad = relativedelta(datetime.now(), est.fecha_nacimiento)
        print(est.nombre)
        print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        for i in datos:

            if est.nombre == i.EvaluacionD.Estudiante.nombre:
                contador += 1

                #fecha_naci = datetime.strptime(est.fecha_nacimiento, "%d/%m/%Y")

                worksheet .write(col, row,   "Evaluacion Destreza 1")
                if contador == 1:
                    worksheet .write(col, row,   "Evaluacion Destreza 1")
                    worksheet.write(col+1, row, 'DIBUJO')
                    worksheet.write(col+2, row, i.D1)
                    worksheet.write(col+1, row+1, 'PRESION SOBRE EL PAPEL')
                    worksheet.write(col+2, row+1, i.D10)
                    worksheet.write(col+1, row+2, 'TIPO DE AGARRE')
                    worksheet.write(col+2, row+2, i.D11)
                    worksheet.write(col+1, row+3, 'DIRECCIONALIDAD')
                    worksheet.write(col+2, row+3, i.D12)
                    worksheet.write(col+1, row+4, 'ESTADO DE ANIMO')
                    worksheet.write(col+2, row+4, i.D13)
                    worksheet.write(col+1, row+5, 'MOVIMIENTO MANO DEDOS')
                    worksheet.write(col+2, row+5, i.D14)
                else:
                    worksheet .write(col, row+9,   "Evaluacion Destreza 1")
                    worksheet.write(col+1, row+9, 'DIBUJO')
                    worksheet.write(col+2, row+9, i.D1)
                    worksheet.write(col+1, row+10, 'PRESION SOBRE EL PAPEL')
                    worksheet.write(col+2, row+10, i.D10)
                    worksheet.write(col+1, row+11, 'TIPO DE AGARRE')
                    worksheet.write(col+2, row+11, i.D11)
                    worksheet.write(col+1, row+12, 'DIRECCIONALIDAD')
                    worksheet.write(col+2, row+12, i.D12)
                    worksheet.write(col+1, row+13, 'ESTADO DE ANIMO')
                    worksheet.write(col+2, row+13, i.D13)
                    worksheet.write(col+1, row+14, 'MOVIMIENTO MANO DEDOS')
                    worksheet.write(col+2, row+14, i.D14)
        datos2 = EvaluacionD2.objects.order_by("id")
        contador = 0
        for j in datos2:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1

             
                if contador == 1:
                    worksheet .write(col+3, row,   "Evaluacion Destreza 2")
                    worksheet.write(col+4, row, j.D2)
                    worksheet.write(col+4, row+1, j.D10)
                    worksheet.write(col+4, row+2, j.D11)
                    worksheet.write(col+4, row+3, j.D12)
                    worksheet.write(col+4, row+4, j.D13)
                    worksheet.write(col+4, row+5, j.D14)
                else:
                    worksheet .write(col+3, row+9,   "Evaluacion Destreza 2")
                    worksheet.write(col+4, row+9, j.D2)
                    worksheet.write(col+4, row+10, j.D10)
                    worksheet.write(col+4, row+11, j.D11)
                    worksheet.write(col+4, row+12, j.D12)
                    worksheet.write(col+4, row+13, j.D13)
                    worksheet.write(col+4, row+14, j.D14)

        datos3 = EvaluacionD3.objects.order_by("id")
        contador = 0
        for j in datos3:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+5, row,   "Evaluacion Destreza 3")
                    worksheet .write(col+6, row, j.D3)
                    worksheet .write(col+6, row+1, j.D10)
                    worksheet .write(col+6, row+2, j.D11)
                    worksheet .write(col+6, row+3, j.D12)
                    worksheet .write(col+6, row+4, j.D13)
                    worksheet .write(col+6, row+5, j.D14)

                else:
                    worksheet .write(col+5, row+9,   "Evaluacion Destreza 3")
                    worksheet .write(col+6, row+9, j.D3)
                    worksheet .write(col+6, row+10, j.D10)
                    worksheet .write(col+6, row+11, j.D11)
                    worksheet .write(col+6, row+12, j.D12)
                    worksheet .write(col+6, row+13, j.D13)
                    worksheet .write(col+6, row+14, j.D14)

        datos4 = EvaluacionD4.objects.order_by("id")
        contador = 0
        for j in datos4:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+7, row,   "Evaluacion Destreza 4")
                    worksheet .write(col+8, row, j.D4)
                    worksheet .write(col+8, row+1, j.D10)
                    worksheet .write(col+8, row+2, j.D11)
                    worksheet .write(col+8, row+3, j.D12)
                    worksheet .write(col+8, row+4, j.D13)
                    worksheet .write(col+8, row+5, j.D14)

                else:
                    worksheet .write(col+7, row+9,   "Evaluacion Destreza 4")
                    worksheet .write(col+8, row+9, j.D4)
                    worksheet .write(col+8, row+10, j.D10)
                    worksheet .write(col+8, row+11, j.D11)
                    worksheet .write(col+8, row+12, j.D12)
                    worksheet .write(col+8, row+13, j.D13)
                    worksheet .write(col+8, row+14, j.D14)

        datos5 = EvaluacionD5.objects.order_by("id")
        contador = 0
        for j in datos5:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+9, row,   "Evaluacion Destreza 5")
                    worksheet .write(col+10, row, j.D5)
                    worksheet .write(col+10, row+1, j.D10)
                    worksheet .write(col+10, row+2, j.D11)
                    worksheet .write(col+10, row+3, j.D12)
                    worksheet .write(col+10, row+4, j.D13)
                    worksheet .write(col+10, row+5, j.D14)
                else:
                    worksheet .write(col+9, row+9,   "Evaluacion Destreza 5")
                    worksheet .write(col+10, row+9, j.D5)
                    worksheet .write(col+10, row+10, j.D10)
                    worksheet .write(col+10, row+11, j.D11)
                    worksheet .write(col+10, row+12, j.D12)
                    worksheet .write(col+10, row+13, j.D13)
                    worksheet .write(col+10, row+14, j.D14)

        datos6 = EvaluacionD6.objects.order_by("id")
        contador = 0
        for j in datos6:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+11, row,   "Evaluacion Destreza 6")
                    worksheet .write(col+12, row, j.D6)
                    worksheet .write(col+12, row+1, j.D10)
                    worksheet .write(col+12, row+2, j.D11)
                    worksheet .write(col+12, row+3, j.D12)
                    worksheet .write(col+12, row+4, j.D13)
                    worksheet .write(col+12, row+5, j.D14)
                else:
                    worksheet .write(col+11, row+9,   "Evaluacion Destreza 6")
                    worksheet .write(col+12, row+9, j.D6)
                    worksheet .write(col+12, row+10, j.D10)
                    worksheet .write(col+12, row+11, j.D11)
                    worksheet .write(col+12, row+12, j.D12)
                    worksheet .write(col+12, row+13, j.D13)
                    worksheet .write(col+12, row+14, j.D14)

        datos7 = EvaluacionD7.objects.order_by("id")
        contador = 0
        for j in datos7:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+13, row,   "Evaluacion Destreza 7")
                    worksheet .write(col+14, row, j.D7)
                    worksheet .write(col+14, row+1, j.D10)
                    worksheet .write(col+14, row+2, j.D11)
                    worksheet .write(col+14, row+3, j.D12)
                    worksheet .write(col+14, row+4, j.D13)
                    worksheet .write(col+14, row+5, j.D14)
                else:
                    worksheet .write(col+13, row+9,   "Evaluacion Destreza 7")
                    worksheet .write(col+14, row+9, j.D7)
                    worksheet .write(col+14, row+10, j.D10)
                    worksheet .write(col+14, row+11, j.D11)
                    worksheet .write(col+14, row+12, j.D12)
                    worksheet .write(col+14, row+13, j.D13)
                    worksheet .write(col+14, row+14, j.D14)

        datos8 = EvaluacionD8.objects.order_by("id")
        contador = 0
        for j in datos8:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+15, row,   "Evaluacion Destreza 8")
                    worksheet .write(col+16, row, j.D8)
                    worksheet .write(col+16, row+1, j.D10)
                    worksheet .write(col+16, row+2, j.D11)
                    worksheet .write(col+16, row+3, j.D12)
                    worksheet .write(col+16, row+4, j.D13)
                    worksheet .write(col+16, row+5, j.D14)
                else:
                    worksheet .write(col+15, row+9,   "Evaluacion Destreza 8")
                    worksheet .write(col+16, row+9, j.D8)
                    worksheet .write(col+16, row+10, j.D10)
                    worksheet .write(col+16, row+11, j.D11)
                    worksheet .write(col+16, row+12, j.D12)
                    worksheet .write(col+16, row+13, j.D13)
                    worksheet .write(col+16, row+14, j.D14)
        datos9 = EvaluacionD9.objects.order_by("id")
        contador = 0
        for j in datos9:
            if est.nombre == j.EvaluacionD.Estudiante.nombre:
                contador += 1
                
                if contador == 1:
                    worksheet .write(col+17, row,   "Evaluacion Destreza 9")
                    worksheet .write(col+18, row, j.D9)
                    worksheet .write(col+18, row+1, j.D10)
                    worksheet .write(col+18, row+2, j.D11)
                    worksheet .write(col+18, row+3, j.D12)
                    worksheet .write(col+18, row+4, j.D13)
                    worksheet .write(col+18, row+5, j.D14)
                else:
                    worksheet .write(col+17, row+9,   "Evaluacion Destreza 9")
                    worksheet .write(col+18, row+9, j.D9)
                    worksheet .write(col+18, row+10, j.D10)
                    worksheet .write(col+18, row+11, j.D11)
                    worksheet .write(col+18, row+12, j.D12)
                    worksheet .write(col+18, row+13, j.D13)
                    worksheet .write(col+18, row+14, j.D14)

        worksheet .write(col+20, row,   "Recomendacion Destreza 1")

        if edad.years == 4 or edad.years == 5 or edad.years == 6: 
            for j in RecomendacionD1.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+21, row, 'Frecuencia')
                    worksheet .write(col+21, row+1, 'Semanas')
                    worksheet .write(col+21, row+2, 'AC1')
                    worksheet .write(col+21, row+3, 'AC2')
                    worksheet .write(col+21, row+4, 'AC3')
                    worksheet .write(col+21, row+5, 'AC4')
                    worksheet .write(col+21, row+6, 'AC5')
                    worksheet .write(col+21, row+7, 'AC41')
                    worksheet .write(col+21, row+8, 'AC42')

                    worksheet .write(col+22, row, j.FrecuenciaS)
                    worksheet .write(col+22, row+1, j.Semanas)
                    worksheet .write(col+22, row+2, j.AC1)
                    worksheet .write(col+22, row+3, j.AC2)
                    worksheet .write(col+22, row+4, j.AC3)
                    worksheet .write(col+22, row+5, j.AC4)
                    worksheet .write(col+22, row+6, j.AC5)
                    worksheet .write(col+22, row+7, j.AC41)
                    worksheet .write(col+22, row+8, j.AC42)

            worksheet .write(col+23, row,   "Recomendacion Destreza 2")
            for j in RecomendacionD2.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+24, row, 'Frecuencia')
                    worksheet .write(col+24, row+1, 'Semanas')
                    worksheet .write(col+24, row+2, 'AC6')
                    worksheet .write(col+24, row+3, 'AC7')
                    worksheet .write(col+24, row+4, 'AC8')
                    worksheet .write(col+24, row+5, 'AC9')
                    worksheet .write(col+24, row+6, 'AC10')
                    worksheet .write(col+24, row+7, 'AC41')
                    worksheet .write(col+24, row+8, 'AC42')

                    worksheet .write(col+25, row, j.FrecuenciaS)
                    worksheet .write(col+25, row+1, j.Semanas)
                    worksheet .write(col+25, row+2, j.AC6)
                    worksheet .write(col+25, row+3, j.AC7)
                    worksheet .write(col+25, row+4, j.AC8)
                    worksheet .write(col+25, row+5, j.AC9)
                    worksheet .write(col+25, row+6, j.AC10)
                    worksheet .write(col+25, row+7, j.AC41)
                    worksheet .write(col+25, row+8, j.AC42)
            worksheet .write(col+26, row,   "Recomendacion Destreza 3")
            for j in RecomendacionD3.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+27, row, 'Frecuencia')
                    worksheet .write(col+27, row+1, 'Semanas')
                    worksheet .write(col+27, row+2, 'AC11')
                    worksheet .write(col+27, row+3, 'AC12')
                    worksheet .write(col+27, row+4, 'AC13')
                    worksheet .write(col+27, row+5, 'AC14')
                    worksheet .write(col+27, row+6, 'AC15')
                    worksheet .write(col+27, row+7, 'AC41')
                    worksheet .write(col+27, row+8, 'AC42')

                    worksheet .write(col+28, row, j.FrecuenciaS)
                    worksheet .write(col+28, row+1, j.Semanas)
                    worksheet .write(col+28, row+2, j.AC11)
                    worksheet .write(col+28, row+3, j.AC12)
                    worksheet .write(col+28, row+4, j.AC13)
                    worksheet .write(col+28, row+5, j.AC14)
                    worksheet .write(col+28, row+6, j.AC15)
                    worksheet .write(col+28, row+7, j.AC41)
                    worksheet .write(col+28, row+8, j.AC42)
      
        worksheet .write(col+29, row,   "Recomendacion Destreza 4")
        if edad.years == 5 or edad.years == 6: 
            for j in RecomendacionD4.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+30, row, 'Frecuencia')
                    worksheet .write(col+30, row+1, 'Semanas')
                    worksheet .write(col+30, row+2, 'AC16')
                    worksheet .write(col+30, row+3, 'AC17')
                    worksheet .write(col+30, row+4, 'AC18')
                    worksheet .write(col+30, row+5, 'AC19')
                    worksheet .write(col+30, row+6, 'AC20')
                    worksheet .write(col+30, row+7, 'AC39')
                    worksheet .write(col+30, row+8, 'AC40')
                    worksheet .write(col+30, row+9, 'AC41')
                    worksheet .write(col+30, row+10, 'AC42')

                    worksheet .write(col+31, row, j.FrecuenciaS)
                    worksheet .write(col+31, row+1, j.Semanas)
                    worksheet .write(col+31, row+2, j.AC16)
                    worksheet .write(col+31, row+3, j.AC17)
                    worksheet .write(col+31, row+4, j.AC18)
                    worksheet .write(col+31, row+5, j.AC19)
                    worksheet .write(col+31, row+6, j.AC20)
                    worksheet .write(col+31, row+7, j.AC39)
                    worksheet .write(col+31, row+8, j.AC40)
                    worksheet .write(col+31, row+9, j.AC41)
                    worksheet .write(col+31, row+10, j.AC42)
            worksheet .write(col+32, row,   "Recomendacion Destreza 5")
            for j in RecomendacionD5.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+33, row, 'Frecuencia')
                    worksheet .write(col+33, row+1, 'Semanas')
                    worksheet .write(col+33, row+2, 'AC21')
                    worksheet .write(col+33, row+3, 'AC22')
                    worksheet .write(col+33, row+4, 'AC23')
                    worksheet .write(col+33, row+5, 'AC24')
                    worksheet .write(col+33, row+6, 'AC39')
                    worksheet .write(col+33, row+7, 'AC40')
                    worksheet .write(col+33, row+8, 'AC41')
                    worksheet .write(col+33, row+9, 'AC42')

                    worksheet .write(col+34, row, j.FrecuenciaS)
                    worksheet .write(col+34, row+1, j.Semanas)
                    worksheet .write(col+34, row+2, j.AC21)
                    worksheet .write(col+34, row+3, j.AC22)
                    worksheet .write(col+34, row+4, j.AC23)
                    worksheet .write(col+34, row+5, j.AC24)
                    worksheet .write(col+34, row+6, j.AC39)
                    worksheet .write(col+34, row+7, j.AC40)
                    worksheet .write(col+34, row+8, j.AC41)
                    worksheet .write(col+34, row+9, j.AC42)
            worksheet .write(col+35, row,   "Recomendacion Destreza 6")
            for j in RecomendacionD6.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+36, row, 'Frecuencia')
                    worksheet .write(col+36, row+1, 'Semanas')
                    worksheet .write(col+36, row+2, 'AC25')
                    worksheet .write(col+36, row+3, 'AC26')
                    worksheet .write(col+36, row+4, 'AC27')
                    worksheet .write(col+36, row+5, 'AC28')
                    worksheet .write(col+36, row+6, 'AC39')
                    worksheet .write(col+36, row+7, 'AC40')
                    worksheet .write(col+36, row+8, 'AC41')
                    worksheet .write(col+36, row+9, 'AC42')

                    worksheet .write(col+37, row, j.FrecuenciaS)
                    worksheet .write(col+37, row+1, j.Semanas)
                    worksheet .write(col+37, row+2, j.AC25)
                    worksheet .write(col+37, row+3, j.AC26)
                    worksheet .write(col+37, row+4, j.AC27)
                    worksheet .write(col+37, row+5, j.AC28)
                    worksheet .write(col+37, row+6, j.AC39)
                    worksheet .write(col+37, row+7, j.AC40)
                    worksheet .write(col+37, row+8, j.AC41)
                    worksheet .write(col+37, row+9, j.AC42)
        worksheet .write(col+38, row,   "Recomendacion Destreza 7")
        if edad.years == 5 or edad.years == 6: 
            for j in RecomendacionD7.objects.order_by("id"):

                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+39, row, 'Frecuencia')
                    worksheet .write(col+39, row+1, 'Semanas')
                    worksheet .write(col+39, row+2, 'AC29')
                    worksheet .write(col+39, row+3, 'AC30')
                    worksheet .write(col+39, row+4, 'AC31')
                    worksheet .write(col+39, row+5, 'AC32')
                    worksheet .write(col+39, row+6, 'AC39')
                    worksheet .write(col+39, row+7, 'AC40')
                    worksheet .write(col+39, row+8, 'AC41')
                    worksheet .write(col+39, row+9, 'AC42')

                    worksheet .write(col+40, row, j.FrecuenciaS)
                    worksheet .write(col+40, row+1, j.Semanas)
                    worksheet .write(col+40, row+2, j.AC29)
                    worksheet .write(col+40, row+3, j.AC30)
                    worksheet .write(col+40, row+4, j.AC31)
                    worksheet .write(col+40, row+5, j.AC32)
                    worksheet .write(col+40, row+6, j.AC39)
                    worksheet .write(col+40, row+7, j.AC40)
                    worksheet .write(col+40, row+8, j.AC41)
                    worksheet .write(col+40, row+9, j.AC42)

            worksheet .write(col+41, row,   "Recomendacion Destreza 8")
            for j in RecomendacionD8.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+42, row, 'Frecuencia')
                    worksheet .write(col+42, row+1, 'Semanas')
                    worksheet .write(col+42, row+2, 'AC1')
                    worksheet .write(col+42, row+3, 'AC2')
                    worksheet .write(col+42, row+4, 'AC3')
                    worksheet .write(col+42, row+5, 'AC4')
                    worksheet .write(col+42, row+6, 'AC5')
                    worksheet .write(col+42, row+7, 'AC6')
                    worksheet .write(col+42, row+8, 'AC7')
                    worksheet .write(col+42, row+9, 'AC8')
                    worksheet .write(col+42, row+10, 'AC9')
                    worksheet .write(col+42, row+11, 'AC10')
                    worksheet .write(col+42, row+12, 'AC39')
                    worksheet .write(col+42, row+13, 'AC40')
                    worksheet .write(col+42, row+14, 'AC41')
                    worksheet .write(col+42, row+15, 'AC42')

                    worksheet .write(col+43, row, j.FrecuenciaS)
                    worksheet .write(col+43, row+1, j.Semanas)
                    worksheet .write(col+43, row+2, j.AC1)
                    worksheet .write(col+43, row+3, j.AC2)
                    worksheet .write(col+43, row+4, j.AC3)
                    worksheet .write(col+43, row+5, j.AC4)
                    worksheet .write(col+43, row+6, j.AC5)
                    worksheet .write(col+43, row+7, j.AC6)
                    worksheet .write(col+43, row+8, j.AC7)
                    worksheet .write(col+43, row+9, j.AC8)
                    worksheet .write(col+43, row+10, j.AC9)
                    worksheet .write(col+43, row+11, j.AC10)
                    worksheet .write(col+43, row+12, j.AC39)
                    worksheet .write(col+43, row+13, j.AC40)
                    worksheet .write(col+43, row+14, j.AC41)
                    worksheet .write(col+43, row+15, j.AC42)

            worksheet .write(col+44, row,   "Recomendacion Destreza 9")
            for j in RecomendacionD9.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+45, row, 'Frecuencia')
                    worksheet .write(col+45, row+1, 'Semanas')
                    worksheet .write(col+45, row+2, 'AC6')
                    worksheet .write(col+45, row+3, 'AC7')
                    worksheet .write(col+45, row+4, 'AC8')
                    worksheet .write(col+45, row+5, 'AC9')
                    worksheet .write(col+45, row+6, 'AC10')
                    worksheet .write(col+45, row+7, 'AC34')
                    worksheet .write(col+45, row+8, 'AC35')
                    worksheet .write(col+45, row+9, 'AC36')
                    worksheet .write(col+45, row+10, 'AC37')
                    worksheet .write(col+45, row+11, 'AC38')
                    worksheet .write(col+45, row+12, 'AC39')
                    worksheet .write(col+45, row+13, 'AC40')
                    worksheet .write(col+45, row+14, 'AC41')
                    worksheet .write(col+45, row+15, 'AC42')

                    worksheet .write(col+46, row, j.FrecuenciaS)
                    worksheet .write(col+46, row+1, j.Semanas)
                    worksheet .write(col+46, row+2, j.AC6)
                    worksheet .write(col+46, row+3, j.AC7)
                    worksheet .write(col+46, row+4, j.AC8)
                    worksheet .write(col+46, row+5, j.AC9)
                    worksheet .write(col+46, row+6, j.AC10)
                    worksheet .write(col+46, row+7, j.AC34)
                    worksheet .write(col+46, row+8, j.AC35)
                    worksheet .write(col+46, row+9, j.AC36)
                    worksheet .write(col+46, row+10, j.AC37)
                    worksheet .write(col+46, row+11, j.AC38)
                    worksheet .write(col+46, row+12, j.AC39)
                    worksheet .write(col+46, row+13, j.AC40)
                    worksheet .write(col+46, row+14, j.AC41)
                    worksheet .write(col+46, row+15, j.AC42)
        row = 18
        worksheet .write(col+20, row,   "Seguimiento Destreza 1")
        if edad.years == 4 or edad.years == 5 or edad.years == 6: 
            for j in RecomendacionD1S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+21, row, 'Frecuencia')
                    worksheet .write(col+21, row+1, 'Semanas')
                    worksheet .write(col+21, row+2, 'AC1')
                    worksheet .write(col+21, row+3, 'AC2')
                    worksheet .write(col+21, row+4, 'AC3')
                    worksheet .write(col+21, row+5, 'AC4')
                    worksheet .write(col+21, row+6, 'AC5')
                    worksheet .write(col+21, row+7, 'AC41')
                    worksheet .write(col+21, row+8, 'AC42')

                    worksheet .write(col+22, row, j.FrecuenciaS)
                    worksheet .write(col+22, row+1, j.Semanas)
                    worksheet .write(col+22, row+2, j.AC1)
                    worksheet .write(col+22, row+3, j.AC2)
                    worksheet .write(col+22, row+4, j.AC3)
                    worksheet .write(col+22, row+5, j.AC4)
                    worksheet .write(col+22, row+6, j.AC5)
                    worksheet .write(col+22, row+7, j.AC41)
                    worksheet .write(col+22, row+8, j.AC42)
            worksheet .write(col+23, row,   "Seguimiento Destreza 2")
            for j in RecomendacionD2S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+24, row, 'Frecuencia')
                    worksheet .write(col+24, row+1, 'Semanas')
                    worksheet .write(col+24, row+2, 'AC6')
                    worksheet .write(col+24, row+3, 'AC7')
                    worksheet .write(col+24, row+4, 'AC8')
                    worksheet .write(col+24, row+5, 'AC9')
                    worksheet .write(col+24, row+6, 'AC10')
                    worksheet .write(col+24, row+7, 'AC41')
                    worksheet .write(col+24, row+8, 'AC42')

                    worksheet .write(col+25, row, j.FrecuenciaS)
                    worksheet .write(col+25, row+1, j.Semanas)
                    worksheet .write(col+25, row+2, j.AC6)
                    worksheet .write(col+25, row+3, j.AC7)
                    worksheet .write(col+25, row+4, j.AC8)
                    worksheet .write(col+25, row+5, j.AC9)
                    worksheet .write(col+25, row+6, j.AC10)
                    worksheet .write(col+25, row+7, j.AC41)
                    worksheet .write(col+25, row+8, j.AC42)
            worksheet .write(col+26, row,   "Seguimiento Destreza 3")
            for j in RecomendacionD3S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+27, row, 'Frecuencia')
                    worksheet .write(col+27, row+1, 'Semanas')
                    worksheet .write(col+27, row+2, 'AC11')
                    worksheet .write(col+27, row+3, 'AC12')
                    worksheet .write(col+27, row+4, 'AC13')
                    worksheet .write(col+27, row+5, 'AC14')
                    worksheet .write(col+27, row+6, 'AC15')
                    worksheet .write(col+27, row+7, 'AC41')
                    worksheet .write(col+27, row+8, 'AC42')

                    worksheet .write(col+28, row, j.FrecuenciaS)
                    worksheet .write(col+28, row+1, j.Semanas)
                    worksheet .write(col+28, row+2, j.AC11)
                    worksheet .write(col+28, row+3, j.AC12)
                    worksheet .write(col+28, row+4, j.AC13)
                    worksheet .write(col+28, row+5, j.AC14)
                    worksheet .write(col+28, row+6, j.AC15)
                    worksheet .write(col+28, row+7, j.AC41)
                    worksheet .write(col+28, row+8, j.AC42)
        worksheet .write(col+29, row,   "Segimiento Destreza 4")
        if edad.years == 5 or edad.years == 6: 
            for j in RecomendacionD4S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+30, row, 'Frecuencia')
                    worksheet .write(col+30, row+1, 'Semanas')
                    worksheet .write(col+30, row+2, 'AC16')
                    worksheet .write(col+30, row+3, 'AC17')
                    worksheet .write(col+30, row+4, 'AC18')
                    worksheet .write(col+30, row+5, 'AC19')
                    worksheet .write(col+30, row+6, 'AC20')
                    worksheet .write(col+30, row+7, 'AC39')
                    worksheet .write(col+30, row+8, 'AC40')
                    worksheet .write(col+30, row+9, 'AC41')
                    worksheet .write(col+30, row+10, 'AC42')

                    worksheet .write(col+31, row, j.FrecuenciaS)
                    worksheet .write(col+31, row+1, j.Semanas)
                    worksheet .write(col+31, row+2, j.AC16)
                    worksheet .write(col+31, row+3, j.AC17)
                    worksheet .write(col+31, row+4, j.AC18)
                    worksheet .write(col+31, row+5, j.AC19)
                    worksheet .write(col+31, row+6, j.AC20)
                    worksheet .write(col+31, row+7, j.AC39)
                    worksheet .write(col+31, row+8, j.AC40)
                    worksheet .write(col+31, row+9, j.AC41)
                    worksheet .write(col+31, row+10, j.AC42)

            worksheet .write(col+32, row,   "Seguimiento Destreza 5")
            for j in RecomendacionD5S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+33, row, 'Frecuencia')
                    worksheet .write(col+33, row+1, 'Semanas')
                    worksheet .write(col+33, row+2, 'AC21')
                    worksheet .write(col+33, row+3, 'AC22')
                    worksheet .write(col+33, row+4, 'AC23')
                    worksheet .write(col+33, row+5, 'AC24')
                    worksheet .write(col+33, row+6, 'AC39')
                    worksheet .write(col+33, row+7, 'AC40')
                    worksheet .write(col+33, row+8, 'AC41')
                    worksheet .write(col+33, row+9, 'AC42')

                    worksheet .write(col+34, row, j.FrecuenciaS)
                    worksheet .write(col+34, row+1, j.Semanas)
                    worksheet .write(col+34, row+2, j.AC21)
                    worksheet .write(col+34, row+3, j.AC22)
                    worksheet .write(col+34, row+4, j.AC23)
                    worksheet .write(col+34, row+5, j.AC24)
                    worksheet .write(col+34, row+6, j.AC39)
                    worksheet .write(col+34, row+7, j.AC40)
                    worksheet .write(col+34, row+8, j.AC41)
                    worksheet .write(col+34, row+9, j.AC42)
            worksheet .write(col+35, row,   "Seguimiento Destreza 6")
            for j in RecomendacionD6S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+36, row, 'Frecuencia')
                    worksheet .write(col+36, row+1, 'Semanas')
                    worksheet .write(col+36, row+2, 'AC25')
                    worksheet .write(col+36, row+3, 'AC26')
                    worksheet .write(col+36, row+4, 'AC27')
                    worksheet .write(col+36, row+5, 'AC28')
                    worksheet .write(col+36, row+6, 'AC39')
                    worksheet .write(col+36, row+7, 'AC40')
                    worksheet .write(col+36, row+8, 'AC41')
                    worksheet .write(col+36, row+9, 'AC42')

                    worksheet .write(col+37, row, j.FrecuenciaS)
                    worksheet .write(col+37, row+1, j.Semanas)
                    worksheet .write(col+37, row+2, j.AC25)
                    worksheet .write(col+37, row+3, j.AC26)
                    worksheet .write(col+37, row+4, j.AC27)
                    worksheet .write(col+37, row+5, j.AC28)
                    worksheet .write(col+37, row+6, j.AC39)
                    worksheet .write(col+37, row+7, j.AC40)
                    worksheet .write(col+37, row+8, j.AC41)
                    worksheet .write(col+37, row+9, j.AC42)
        worksheet .write(col+38, row,   "Seguimiento Destreza 7")
        if  edad.years == 6: 
            for j in RecomendacionD7S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+39, row, 'Frecuencia')
                    worksheet .write(col+39, row+1, 'Semanas')
                    worksheet .write(col+39, row+2, 'AC29')
                    worksheet .write(col+39, row+3, 'AC30')
                    worksheet .write(col+39, row+4, 'AC31')
                    worksheet .write(col+39, row+5, 'AC32')
                    worksheet .write(col+39, row+6, 'AC39')
                    worksheet .write(col+39, row+7, 'AC40')
                    worksheet .write(col+39, row+8, 'AC41')
                    worksheet .write(col+39, row+9, 'AC42')

                    worksheet .write(col+40, row, j.FrecuenciaS)
                    worksheet .write(col+40, row+1, j.Semanas)
                    worksheet .write(col+40, row+2, j.AC29)
                    worksheet .write(col+40, row+3, j.AC30)
                    worksheet .write(col+40, row+4, j.AC31)
                    worksheet .write(col+40, row+5, j.AC32)
                    worksheet .write(col+40, row+6, j.AC39)
                    worksheet .write(col+40, row+7, j.AC40)
                    worksheet .write(col+40, row+8, j.AC41)
                    worksheet .write(col+40, row+9, j.AC42)

            worksheet .write(col+41, row,   "Seguimiento Destreza 8")
            for j in RecomendacionD8S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+42, row, 'Frecuencia')
                    worksheet .write(col+42, row+1, 'Semanas')
                    worksheet .write(col+42, row+2, 'AC1')
                    worksheet .write(col+42, row+3, 'AC2')
                    worksheet .write(col+42, row+4, 'AC3')
                    worksheet .write(col+42, row+5, 'AC4')
                    worksheet .write(col+42, row+6, 'AC5')
                    worksheet .write(col+42, row+7, 'AC6')
                    worksheet .write(col+42, row+8, 'AC7')
                    worksheet .write(col+42, row+9, 'AC8')
                    worksheet .write(col+42, row+10, 'AC9')
                    worksheet .write(col+42, row+11, 'AC10')
                    worksheet .write(col+42, row+12, 'AC39')
                    worksheet .write(col+42, row+13, 'AC40')
                    worksheet .write(col+42, row+14, 'AC41')
                    worksheet .write(col+42, row+15, 'AC42')

                    worksheet .write(col+43, row, j.FrecuenciaS)
                    worksheet .write(col+43, row+1, j.Semanas)
                    worksheet .write(col+43, row+2, j.AC1)
                    worksheet .write(col+43, row+3, j.AC2)
                    worksheet .write(col+43, row+4, j.AC3)
                    worksheet .write(col+43, row+5, j.AC4)
                    worksheet .write(col+43, row+6, j.AC5)
                    worksheet .write(col+43, row+7, j.AC6)
                    worksheet .write(col+43, row+8, j.AC7)
                    worksheet .write(col+43, row+9, j.AC8)
                    worksheet .write(col+43, row+10, j.AC9)
                    worksheet .write(col+43, row+11, j.AC10)
                    worksheet .write(col+43, row+12, j.AC39)
                    worksheet .write(col+43, row+13, j.AC40)
                    worksheet .write(col+43, row+14, j.AC41)
                    worksheet .write(col+43, row+15, j.AC42)

            worksheet .write(col+44, row,   "Seguimiento Destreza 9")
            for j in RecomendacionD9S.objects.order_by("id"):
                if j.RecomendacionEst.Estudiante.nombre == est.nombre:
                    worksheet .write(col+45, row, 'Frecuencia')
                    worksheet .write(col+45, row+1, 'Semanas')
                    worksheet .write(col+45, row+2, 'AC6')
                    worksheet .write(col+45, row+3, 'AC7')
                    worksheet .write(col+45, row+4, 'AC8')
                    worksheet .write(col+45, row+5, 'AC9')
                    worksheet .write(col+45, row+6, 'AC10')
                    worksheet .write(col+45, row+7, 'AC34')
                    worksheet .write(col+45, row+8, 'AC35')
                    worksheet .write(col+45, row+9, 'AC36')
                    worksheet .write(col+45, row+10, 'AC37')
                    worksheet .write(col+45, row+11, 'AC38')
                    worksheet .write(col+45, row+12, 'AC39')
                    worksheet .write(col+45, row+13, 'AC40')
                    worksheet .write(col+45, row+14, 'AC41')
                    worksheet .write(col+45, row+15, 'AC42')

                    worksheet .write(col+46, row, j.FrecuenciaS)
                    worksheet .write(col+46, row+1, j.Semanas)
                    worksheet .write(col+46, row+2, j.AC6)
                    worksheet .write(col+46, row+3, j.AC7)
                    worksheet .write(col+46, row+4, j.AC8)
                    worksheet .write(col+46, row+5, j.AC9)
                    worksheet .write(col+46, row+6, j.AC10)
                    worksheet .write(col+46, row+7, j.AC34)
                    worksheet .write(col+46, row+8, j.AC35)
                    worksheet .write(col+46, row+9, j.AC36)
                    worksheet .write(col+46, row+10, j.AC37)
                    worksheet .write(col+46, row+11, j.AC38)
                    worksheet .write(col+46, row+12, j.AC39)
                    worksheet .write(col+46, row+13, j.AC40)
                    worksheet .write(col+46, row+14, j.AC41)
                    worksheet .write(col+46, row+15, j.AC42)
        row = 0

        col = 50
        info = ['Frecuencia: Frecuencia Semanal', 'Semana: Numero semanas', 'AC1: Completar líneas horizontales trazadas en forma entrecortada', 'AC2: Seguir laberintos trazando líneas horizontales',
                'AC3: Unir dos puntos para formas líneas horizontales', 'AC4: Punzar líneas horizontales grandes y pequeñas', 'AC5: Copiar en la pizarra o en el papel cuadriculado líneas horizontales',
                'AC6: Completar líneas verticales trazadas en forma entrecortada', 'AC7: Seguir laberintos trazando líneas verticales y horizontales', 'AC8: Unir dos puntos para formas líneas verticales',
                'AC9: Punzar líneas verticales grandes y pequeñas', 'AC10: Copiar en la pizarra o en el papel cuadriculado líneas verticales', 'AC11: Completar los círculos trazados de forma entrecortada',
                'AC12: Completar los semicírculos trazados de forma entrecortada', 'AC13: Punzar siguiendo el trazo del círculo', 'AC14: Unir los puntos para formar el círculo', 'AC15: Seguir el contorno de  bucles ascendentes y descendentes',
                'AC16: Completar los cuadrados trazados en forma entrecortada', 'AC17: Punzar siguiendo el trazo del cuadrado', 'AC18: Unir los puntos para formar el cuadrado', 'AC19: Seguir caminos trazados en forma de L',
                'AC20: Trazar el cuadrado en el papel cuadriculado', 'AC21: Copiar en la pizarra o papel cuadriculado una cruz', 'AC22: Unir los puntos trazados para formar una cruz', 'AC23: Completar las cruces dibujadas de forma entrecortada',
                'AC24: Punzar las cruces dibujadas', 'AC25: Completar los triángulos trazados en forma entrecortada', 'AC26: Punzar siguiendo el trazo del triángulo', 'AC27: Unir los puntos para formar el triángulo',
                'AC28: Seguir los caminos en zig-zag', 'AC29: Completar líneas onduladas trazadas de forma entrecortada', 'AC30: Seguir el trazo de los bucles ascendentes o descendentes', 'AC31: Realizar ondas o blucles dentro de dos líneas, sobre ejes horizontales, verticales o inclinados',
                'AC32: Seguir el trazo de la letra /m/ /n/ manuscrita en forma continua', 'AC34: Completar líneas oblícuas trazadas en forma entrecortada', 'AC35: Seguir laberintos trazando líneas oblicuas',
                'AC36: Unir dos puntos para formas líneas oblicuas', 'AC37: Punzar líneas oblicuas grandes y pequeñas', 'AC38: Copiar en la pizarra o en el papel cuadriculado líneas oblicuas',
                'AC39: Juegos', 'AC40: Dos actividades', 'AC41: Dos actividades', 'AC42: Juegos serios con lápiz- libre - dos'
                ]
        for li in info:
            worksheet .write(col, row, li)
            col += 1
        col = 0
    workbook.close()
    xlsx_data = output.getvalue()
    resp.write(xlsx_data)
    return resp


@api_view(['PUT'])
def EvaluacionD1S_Post(request, id):
    if request.method == 'PUT':
        print(id)
        tutorial = RecomendacionD1S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD1SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response('Update Error',status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD2S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD2S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD2SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD3S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD3S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD3SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD4S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD4S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD4SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD5S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD5S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD5SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD6S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD6S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD6SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD7S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD7S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD7SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD8S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD8S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD8SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def EvaluacionD9S_Post(request, id):
    if request.method == 'PUT':
        tutorial = RecomendacionD9S.objects.get(id=id)
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RecomendacionD9SSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # cambiar esto
        # return Response(tutorial_serializer.data,status=status.HTTP_201_CREATED) en el servidor de david
