from django.contrib import admin

from .models import IntervencionEst, SesionEst, SesionD1,SesionD2

class IntervencionEstAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','fecha_Inicio','fecha_ultima','Num_Ses')

admin.site.register(IntervencionEst, IntervencionEstAdmin)

admin.site.register(SesionEst)

admin.site.register(SesionD1)

admin.site.register(SesionD2)


# Register your models here.
