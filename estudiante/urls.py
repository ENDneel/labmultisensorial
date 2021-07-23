from django.urls import path, include 
from . import views
from dashboard.views import EstChartView,ListEstudent
from .views import EstudentDetail,EstudenUpdateView,EstudentListView
from rest_framework import routers

from .viewsets import EstudianteViewSet

router = routers.SimpleRouter()
router.register(r'estudiante', EstudianteViewSet)

urlpatterns = [
    #path('',views.dashboard),
    path('estudent/<int:pk>',EstudentDetail,name='detailEstudent'),
    path('<int:pk>/update',EstudenUpdateView.as_view(),name='updateEst'),
    path('estudent/', EstudentListView.as_view(), name='Estudent_List'),
]
urlpatterns += router.urls