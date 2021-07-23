from rest_framework import routers
from .viewsets import EvaluacionDViewSet, EvaluacionD1ViewSet, EvaluacionD2ViewSet , EvaluacionD3ViewSet , EvaluacionD4ViewSet , EvaluacionD5ViewSet , EvaluacionD6ViewSet , EvaluacionD7ViewSet , EvaluacionD8ViewSet , EvaluacionD9ViewSet
from django.urls import path
from . import views


router = routers.SimpleRouter()
router.register('evaluacionD', EvaluacionDViewSet)
router.register('evaluacionD1', EvaluacionD1ViewSet)
router.register('evaluacionD2', EvaluacionD2ViewSet)
router.register('evaluacionD3', EvaluacionD3ViewSet)
router.register('evaluacionD4', EvaluacionD4ViewSet)
router.register('evaluacionD5', EvaluacionD5ViewSet)
router.register('evaluacionD6', EvaluacionD6ViewSet)
router.register('evaluacionD7', EvaluacionD7ViewSet)
router.register('evaluacionD8', EvaluacionD8ViewSet)
router.register('evaluacionD9', EvaluacionD9ViewSet)

urlpatterns = [
    path('evaluacionPost/', views.EvaluacionD_Post),
    path('evaluacionD1_Post/', views.EvaluacionD1_Post),
    path('evaluacionD2_Post/', views.EvaluacionD2_Post),
    path('evaluacionD3_Post/', views.EvaluacionD3_Post),
    path('evaluacionD4_Post/', views.EvaluacionD4_Post),
    path('evaluacionD5_Post/', views.EvaluacionD5_Post),
    path('evaluacionD6_Post/', views.EvaluacionD6_Post),
    path('evaluacionD7_Post/', views.EvaluacionD7_Post),
    path('evaluacionD8_Post/', views.EvaluacionD8_Post),
    path('evaluacionD9_Post/', views.EvaluacionD9_Post),
]

urlpatterns += router.urls
