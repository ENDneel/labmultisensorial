from rest_framework import routers
from .viewsets import *
from django.urls import path
from .views import *
router = routers.SimpleRouter()
router.register('recomendacionD1S', RecomendacionD1SViewSet)
router.register('recomendacionD2S', RecomendacionD2SViewSet)
router.register('recomendacionD3S', RecomendacionD3SViewSet)
router.register('recomendacionD4S', RecomendacionD4SViewSet)
router.register('recomendacionD5S', RecomendacionD5SViewSet)
router.register('recomendacionD6S', RecomendacionD6SViewSet)
router.register('recomendacionD7S', RecomendacionD7SViewSet)
router.register('recomendacionD8S', RecomendacionD8SViewSet)
router.register('recomendacionD9S', RecomendacionD9SViewSet)

urlpatterns = [
    path(r'EvaluacionD1S_Post/<int:id>',EvaluacionD1S_Post),
    path(r'EvaluacionD2S_Post/<int:id>',EvaluacionD2S_Post),
    path(r'EvaluacionD3S_Post/<int:id>',EvaluacionD3S_Post),
    path(r'EvaluacionD4S_Post/<int:id>',EvaluacionD4S_Post),
    path(r'EvaluacionD5S_Post/<int:id>',EvaluacionD5S_Post),
    path(r'EvaluacionD6S_Post/<int:id>',EvaluacionD6S_Post),
    path(r'EvaluacionD7S_Post/<int:id>',EvaluacionD7S_Post),
    path(r'EvaluacionD8S_Post/<int:id>',EvaluacionD8S_Post),
    path(r'EvaluacionD9S_Post/<int:id>',EvaluacionD9S_Post),
    path('desca/', index)
]
urlpatterns += router.urls