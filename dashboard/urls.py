from django.urls import path, include 
from . import views
from dashboard.views import EstChartView,ListEstudent,EstudentDetail
urlpatterns = [
    #path('',views.dashboard),
    path('',EstChartView.as_view(),name='dashboard'),
    path('estudent/',ListEstudent,name='addEstudent'),
   # path('estudent/<int:pk>',EstudentDetail.as_view(),name='detailEstudent'),

    
    
]