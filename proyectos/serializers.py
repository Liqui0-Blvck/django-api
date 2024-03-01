from rest_framework import serializers
from .models import *
from django.contrib.contenttypes.models import *

class ServicioProyectoTipoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = ServicioProyectoTipo
    fields = '__all__'

class ServiciosEnProyectoSerializer(serializers.ModelSerializer):
  tipo = ServicioProyectoTipoSerializer(many=True, read_only = True, source = 'servicioproyectotipo_set')
  class Meta:
    model = ServicioEnProyecto
    fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
  servicios = ServiciosEnProyectoSerializer(many=True, read_only = True, source = 'servicioenproyecto_set')
  class Meta:
    model = Proyecto
    fields = '__all__'
    
  
class BaseProyectoTipoSerializer(serializers.ModelSerializer):
  bases = ServicioProyectoTipoSerializer(many = True, read_only = True, source = 'servicioproyectotipo_set')
  class Meta:
    model = BasesProyectoTipo
    fields = '__all__'
  
class ServicioProyectoPersonalizadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServicioProyectoPersonalizado
    fields = '__all__'
    
class ContentTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContentType
    fields = '__all__'