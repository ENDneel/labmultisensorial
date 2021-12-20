from django.urls import path, include

from modulos.views import CuboTemplateView, LapizDetailView, ModulosView, MotricidadGView, MotricidadPView, StemView 

urlpatterns = [
    path('modulos/',ModulosView.as_view(),name='modulos'),
    path('stem/',StemView.as_view(),name='stem'),
    path('modulos/lapiz/<pk>/', LapizDetailView.as_view(), name='lapiz-detail'),
    path('modulos/cubo/<pk>/', CuboTemplateView.as_view(), name='cubo-detail'),
    path('modulos/motricidadG/<pk>/', MotricidadGView.as_view(), name='motricidadG-detail'),
     path('modulos/motricidadP/<pk>/', MotricidadPView.as_view(), name='motricidadP-detail'),
    
]