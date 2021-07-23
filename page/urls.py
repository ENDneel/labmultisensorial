from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="inicio"),
    path('acerca/',views.acerca, name="acerca"),
    path('prototipo1a/',views.prototipo1a, name="prototipo1a"),
    path('prototipo1b/',views.prototipo1b, name="prototipo1b"),
    path('prototipo2a/',views.prototipo2a, name="prototipo2a"),
    path('prototipo2b/',views.prototipo2b, name="prototipo2b"),
    path('juegos/',views.juegos, name="juegos"),
    path('sistema/',views.sistema, name="sistema"),
    path('contactos/',views.contactos, name="contactos"),
]