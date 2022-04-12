from django.urls import path, include 
from . import views
from dashboard.views import EstChartView,ListEstudent
from .views import EstudentDetail,FormularioUpdateView,EstudentListView,EstudianteUpdateView
from rest_framework import routers

from .viewsets import EstudianteViewSet

router = routers.SimpleRouter()
router.register(r'estudiante', EstudianteViewSet)

urlpatterns = [
    #path('',views.dashboard),
    path('estudent/<int:pk>',EstudentDetail,name='detailEstudent'),
    path('estudent/<int:pk>/update',EstudianteUpdateView.as_view(),name='EstudianteUpdate'),
    path('estudent/formulario/<int:pk>/update',FormularioUpdateView.as_view(),name='formularioUpdate'),
    path('estudent/', EstudentListView.as_view(), name='Estudent_List'),
]
urlpatterns += router.urls