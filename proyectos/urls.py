from django.urls import path
from .views import *

urlpatterns = [
    path('proyectos/', ProyectoListCreateAPIView.as_view()),
    # path('servicios/', ServicioListCreateAPIView.as_view()),
    path('proyecto-base/', BaseProyectoTipoListCreateAPIView.as_view()),
    path('servicios-tipo/', ServicioProyectoTipoListCreateAPIView.as_view()),
    
]
