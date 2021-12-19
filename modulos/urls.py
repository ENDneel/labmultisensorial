from django.urls import path, include

from modulos.views import CuboTemplateView, LapizDetailView, ModulosView 

urlpatterns = [
    path('modulos/',ModulosView.as_view(),name='modulos'),
    path('modulos/lapiz/<pk>/', LapizDetailView.as_view(), name='lapiz-detail'),
    path('modulos/cubo/<pk>/', CuboTemplateView.as_view(), name='cubo-detail')
    
]