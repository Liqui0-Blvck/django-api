from django.urls import path
from .views import *

urlpatterns = [
    path('proyectos/', ProyectoListCreateAPIView.as_view()),
    path("proyecto/<int:id>", ProyectoUpdateDeleteAPIView.as_view(), name=""),
    path("proyectos-delete/", ProyectoUpdateDeleteAPIView.as_view(), name="eliminar-proyectos"),
    path("servicio-en-proyecto/", ServicioEnProyectoAPIView.as_view()),
    path('proyecto-base/', BaseProyectoTipoListCreateAPIView.as_view()),
    path('servicios-tipo/', ServicioProyectoTipoListCreateAPIView.as_view()),
    path('servicio-personalizado/', ServicioProyectoPersonalizadoListCreateAPIView.as_view()),
    path('content-types/', ContentTypeListAPIView.as_view())
    
]
