from django.contrib import admin
from .models import RecomendacionEst, RecomendacionD1, RecomendacionD2, RecomendacionD3, RecomendacionD4, RecomendacionD5, RecomendacionD6, RecomendacionD7, RecomendacionD8, RecomendacionD9

# Register your models here.


class RecomendacionEstAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante')
admin.site.register(RecomendacionEst,RecomendacionEstAdmin)

class RecomendacionD1Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC1','AC2','AC3','AC4','AC5','AC41','AC42')
admin.site.register(RecomendacionD1,RecomendacionD1Admin)

class RecomendacionD2Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC6','AC7','AC8','AC9','AC10','AC41','AC42')
admin.site.register(RecomendacionD2,RecomendacionD2Admin)


class RecomendacionD3Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC11','AC12','AC13','AC14','AC15','AC41','AC42')
admin.site.register(RecomendacionD3,RecomendacionD3Admin)


class RecomendacionD4Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC16','AC17','AC18','AC19','AC20','AC41','AC42')
admin.site.register(RecomendacionD4,RecomendacionD4Admin)

class RecomendacionD5Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC21','AC22','AC23','AC24','AC39','AC40','AC41','AC42')
admin.site.register(RecomendacionD5,RecomendacionD5Admin)

class RecomendacionD6Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC25','AC26','AC27','AC28','AC39','AC40','AC41','AC42')
admin.site.register(RecomendacionD6,RecomendacionD6Admin)

class RecomendacionD7Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC29','AC30','AC31','AC32','AC41','AC42')
admin.site.register(RecomendacionD7,RecomendacionD7Admin)

class RecomendacionD8Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC1','AC2','AC3','AC4','AC5','AC6','AC7','AC8','AC9','AC10','AC41','AC42')
admin.site.register(RecomendacionD8,RecomendacionD8Admin)

class RecomendacionD9Admin(admin.ModelAdmin):
    pass
    list_display=('id','RecomendacionEst','FrecuenciaS','Semanas','AC6','AC7','AC8','AC9','AC10','AC34','AC35','AC36','AC37','AC38','AC41','AC42')
admin.site.register(RecomendacionD9,RecomendacionD9Admin)
#aqui poner las demas destresas