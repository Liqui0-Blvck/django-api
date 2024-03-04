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
  lookup_field = 'id'
  
  def update(self, request, *args, **kwargs): 
    instance = self.get_object()
    serializer_proyecto = self.get_serializer(instance, data = request.data)
    

    if serializer_proyecto.is_valid():
      servicios = request.data.get('servicios', [])
      servicios_ids_en_request = [servicio.get('id') for servicio in servicios]
      servicios_existentes = list(instance.servicioenproyecto_set.values_list('id', flat=True))
      servicios_eliminables = set(servicios_existentes) - set(servicios_ids_en_request)
      ServicioEnProyecto.objects.filter(id__in = servicios_eliminables).delete()
      
      for servicio in servicios:
        servicio_id = servicio.get('id')

        try:
          servicio_existente = ServicioEnProyecto.objects.get(pk = servicio_id)
          if instance.servicioenproyecto_set.filter(id = servicio_existente.id).exists():
            nuevo_servicio = None
            
            
            ct = ContentType.objects.get(model = servicio_existente.tipo_servicio.model)
            if ct.model == 'servicioproyectotipo':
              nuevo_servicio = ServicioProyectoTipo.objects.get(pk = servicio['id_servicio'])
            elif ct.model == 'servicioproyectopersonalizado':
              nuevo_servicio = ServicioProyectoPersonalizado.objects.get(pk = servicio['id_servicio'])
 
            servicio_existente.id_servicio = nuevo_servicio.pk
            servicio_existente.costo_servicio = servicio.get('costo_servicio')
            servicio_existente.prioridad = servicio.get('prioridad')
            servicio_existente.save()
        except ServicioEnProyecto.DoesNotExist:
          servicio['proyecto'] = instance.pk
          serializer_servicio = ServiciosEnProyectoSerializer(data=servicio)
          
          if serializer_servicio.is_valid():
            serializer_servicio.save()
          else:
            return Response(serializer_servicio.errors, status=HTTP_400_BAD_REQUEST)
      serializer_proyecto.save()
      return Response(serializer_proyecto.data, status=HTTP_200_OK)
    else:
      return Response(serializer_proyecto.errors, status=HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, *args, **kwargs):
    proyectos_ids = request.data.get('ids', [])
    if not proyectos_ids:
        return Response({'error' : 'no se proporcionaron ids validos'}, status=HTTP_400_BAD_REQUEST)
    try:
        self.get_queryset().filter(id__in=proyectos_ids).delete()
        return Response({'success': 'Elimando con exito'}, status=HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'Error al eliminar items: {str(e)}'}, status=HTTP_500_INTERNAL_SERVER_ERROR)  
      

class ServicioEnProyectoAPIView(ListCreateAPIView):
  queryset = ServicioEnProyecto.objects.all()
  serializer_class = ServiciosEnProyectoSerializer

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
      bases = request.data.get('servicios_base', [])
      print(bases)
      for servicio in bases:
        servicio['tipo_base'] = base_proyecto.pk
        serializer_servicio = ServicioProyectoTipoSerializer(data = servicio)
        if serializer_servicio.is_valid():
          serializer_servicio.save()
        else:
          base_proyecto.delete()
      return Response(serializer_base.data, status=HTTP_201_CREATED)
    else:
        return Response(serializer_base.errors, status=HTTP_400_BAD_REQUEST)
  
  
class ServicioProyectoPersonalizadoListCreateAPIView(ListCreateAPIView):
  queryset = ServicioProyectoPersonalizado.objects.all()
  serializer_class = ServicioProyectoPersonalizadoSerializer
  
  
class ContentTypeListAPIView(ListAPIView):
  queryset = ContentType.objects.all()
  serializer_class = ContentTypeSerializer
  
  def get_queryset(self):
    models = ['servicioproyectopersonalizado', 'servicioproyectotipo']
    return ContentType.objects.filter(model__in=models)
  
  
  
  
  
  
class EtapaTipoProyectoListCreateAPIView(ListCreateAPIView):
  queryset = EtapasTipoProyecto.objects.all()
  serializer_class = EtapasTipoProyectoSerializer
  


class EtapaEnProyectoListCreateAPIView(ListCreateAPIView):
  queryset = EtapaEnProyecto.objects.all()
  serializer_class = EtapaEnProyectoSerializer