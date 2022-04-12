from django.contrib import admin

from estudiante.models import Estudiante,Cargo,Terapeuta,Formulario

# Register your models here.

admin.site.register(Estudiante);
admin.site.register(Cargo);
admin.site.register(Terapeuta);
admin.site.register(Formulario);
