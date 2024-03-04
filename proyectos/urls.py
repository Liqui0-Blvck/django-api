from django.urls import path
from .views import *

urlpatterns = [
    path('proyectos/', ProyectoListCreateAPIView.as_view(), name='lista-proyectos'),
    path("proyecto/<int:id>", ProyectoUpdateDeleteAPIView.as_view(), name="actualizar-proyecto"),
    path("proyectos-delete/", ProyectoUpdateDeleteAPIView.as_view(), name="eliminar-proyectos"),
    path('base-proyecto/', BaseProyectoTipoListCreateAPIView.as_view(), name='lista-crear-base-proyecto'),
    path('servicios-base/', ServicioProyectoTipoListCreateAPIView.as_view(), name="lista-crear-servicios-base"),
    path("servicio-en-proyecto/", ServicioEnProyectoAPIView.as_view(), name="lista-de-servicios-en-proyectos"),
    path('servicio-personalizado/', ServicioProyectoPersonalizadoListCreateAPIView.as_view(), name="lista-crear-servicio-adicional"),
    path('content-types/', ContentTypeListAPIView.as_view()),
    
    
    
    
    path('etapa-proyecto/', EtapaTipoProyectoListCreateAPIView.as_view()),
    path('etapa-en-proyecto/', EtapaEnProyectoListCreateAPIView.as_view()),
    

]
