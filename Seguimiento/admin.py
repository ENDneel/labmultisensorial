from django.contrib import admin
from .models import *
# Register your models here.
class RecomendacionD1SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC1','AC2','AC3','AC4','AC5','AC41','AC42')
admin.site.register(RecomendacionD1S,RecomendacionD1SAdmin)

class RecomendacionD2SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC6','AC7','AC8','AC9','AC10','AC41','AC42')
admin.site.register(RecomendacionD2S,RecomendacionD2SAdmin)


class RecomendacionD3SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC11','AC12','AC13','AC14','AC15','AC41','AC42')
admin.site.register(RecomendacionD3S,RecomendacionD3SAdmin)


class RecomendacionD4SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC16','AC17','AC18','AC19','AC20','AC41','AC42')
admin.site.register(RecomendacionD4S,RecomendacionD4SAdmin)

class RecomendacionD5SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC21','AC22','AC23','AC24','AC39','AC40','AC41','AC42')
admin.site.register(RecomendacionD5S,RecomendacionD5SAdmin)

class RecomendacionD6SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC25','AC26','AC27','AC28','AC39','AC40','AC41','AC42')
admin.site.register(RecomendacionD6S,RecomendacionD6SAdmin)

class RecomendacionD7SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC29','AC30','AC31','AC32','AC41','AC42')
admin.site.register(RecomendacionD7S,RecomendacionD7SAdmin)

class RecomendacionD8SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC1','AC2','AC3','AC4','AC5','AC6','AC7','AC8','AC9','AC10','AC41','AC42')
admin.site.register(RecomendacionD8S,RecomendacionD8SAdmin)

class RecomendacionD9SAdmin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC6','AC7','AC8','AC9','AC10','AC34','AC35','AC36','AC37','AC38','AC41','AC42')
admin.site.register(RecomendacionD9S,RecomendacionD9SAdmin)
