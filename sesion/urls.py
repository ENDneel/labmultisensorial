from rest_framework import routers
from django.urls import path, include
from .viewsets import SesionViewSet, TableroViewSet
from .views import SesionTableroDetail,TableroView,createSesion


router = routers.SimpleRouter()
router.register(r'sesion', SesionViewSet)
router.register(r'tablero', TableroViewSet)

urlpatterns = [

 path('<int:pk>/',SesionTableroDetail.as_view(),name='sesionGruesa'),
 path('actividad/',TableroView.as_view(),name='tableroActividad'),
 path('actividad2/<int:pk>',createSesion,name='sesioCreate')

]

urlpatterns += router.urls