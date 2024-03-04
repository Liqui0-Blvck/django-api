from rest_framework import serializers
from .models import *
from django.contrib.contenttypes.models import *



class EtapasTipoProyectoSerializer(serializers.ModelSerializer):
  class Meta:
    model = EtapasTipoProyecto
    fields = '__all__'
 
    
class EtapaEnProyectoSerializer(serializers.ModelSerializer):
  class Meta:
    model = EtapaEnProyecto
    fields = '__all__'
  
    
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
  etapas = EtapaEnProyectoSerializer(many=True, read_only = True, source = 'etapaenproyecto_set')
  class Meta:
    model = Proyecto
    fields = '__all__'
    
  
class BaseProyectoTipoSerializer(serializers.ModelSerializer):
  servicios_base = ServicioProyectoTipoSerializer(many = True, read_only = True, source = 'servicioproyectotipo_set')
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
    
    
    
