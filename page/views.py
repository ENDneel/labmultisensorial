from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"page/home.html")

def acerca(request):
    return render(request,"page/info.html")

def sistema(request):
    return render(request,"page/sistema.html")

def prototipo1a(request):
    return render(request,"page/peluche.html")

def prototipo1b(request):
    return render(request,"page/barita.html")

def prototipo2a(request):
    return render(request,"page/Tablero.html")

def prototipo2b(request):
    return render(request,"page/tableroPeluche.html")

def juegos(request):
    return render(request,"page/juegos.html")

def contactos(request):
        return render(request,"page/contacto.html")

