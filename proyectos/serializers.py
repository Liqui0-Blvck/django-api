from rest_framework import serializers
from .models import *

class ServicioProyectoTipoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServicioProyectoTipo
    fields = '__all__'

class ServiciosEnProyectoSerializer(serializers.ModelSerializer):
  tipo = ServicioProyectoTipoSerializer(many=True, read_only=True, source='servicioproyectotipo_set')
  class Meta:
    model = ServicioEnProyecto
    fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
  servicios = ServiciosEnProyectoSerializer(many=True, read_only=True, source='servicioenproyecto_set')
  class Meta:
    model = Proyecto
    fields = '__all__'
    
  
class BaseProyectoTipoSerializer(serializers.ModelSerializer):
  bases = ServicioProyectoTipoSerializer(many = True, read_only = True, source = 'servicioproyectotipo_set')
  class Meta:
    model = BasesProyectoTipo
    fields = '__all__'
    