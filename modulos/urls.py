from django.urls import path, include
from rest_framework import routers

from modulos.views import CuboTemplateView, LapizDetailView, ModulosView, MotricidadGView, MotricidadPView, StemView,ModulosListview,ModulosForm
from modulos.viewsets import SeriosViewSet 

router = routers.SimpleRouter()
router.register(r'serios', SeriosViewSet)
urlpatterns = [
    path('modulos/',ModulosView.as_view(),name='modulos'),
    path('stem/',StemView.as_view(),name='stem'),
    path('modulos/lapiz/<pk>/', LapizDetailView.as_view(), name='lapiz-detail'),
    path('modulos/cubo/<pk>/', CuboTemplateView.as_view(), name='cubo-detail'),
    path('modulos/motricidadG/<pk>/', MotricidadGView.as_view(), name='motricidadG-detail'),
    path('modulos/motricidadP/<pk>/', MotricidadPView.as_view(), name='motricidadP-detail'),
    path('modulos/listaModulos', ModulosListview.as_view(), name='modulos-list'),
    path('modulos/add', ModulosForm.as_view(), name='modulos-form'),
    
]
urlpatterns += router.urls