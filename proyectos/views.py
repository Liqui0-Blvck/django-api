from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.status import *
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class ProyectoListCreateAPIView(ListCreateAPIView):
  queryset = Proyecto.objects.all()
  serializer_class = ProyectoSerializer

class ProyectoUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Proyecto.objects.all()
  serializer_class = ProyectoSerializer
  
  def update(self, request, *args, **kwargs):
    serializer_proyecto = self.get_serializer(data = request.data)

    if serializer_proyecto.is_valid():
      servicios = request.data.get('servicios', [])
      servicios
            
    
    return super().update(request, *args, **kwargs)

class ServicioProyectoTipoListCreateAPIView(ListCreateAPIView):
  queryset = ServicioProyectoTipo.objects.all()
  serializer_class = ServicioProyectoTipoSerializer
  

class BaseProyectoTipoListCreateAPIView(ListCreateAPIView):
  queryset = BasesProyectoTipo.objects.all()
  serializer_class = BaseProyectoTipoSerializer
  
  def create(self, request, *args, **kwargs):
    serializer_base = self.get_serializer(data = request.data)
    if serializer_base.is_valid():
      base_proyecto = serializer_base.save()
      bases = request.data.get('bases', [])
      for servicio in bases:
        servicio['proyecto_tipo'] = base_proyecto.pk
        serializer_servicio = ServicioProyectoTipoSerializer(data = servicio)
        if serializer_servicio.is_valid():
          serializer_servicio.save()
        else:
          base_proyecto.delete()
      return Response(serializer_base.data, status=HTTP_201_CREATED)
    else:
        return Response(serializer_base.errors, status=HTTP_400_BAD_REQUEST)
  
  
