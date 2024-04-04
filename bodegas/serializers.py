from rest_framework import serializers
from .models import *
from controlcalidad.models import *
from controlcalidad.serializers import *



class CCGuiaInternaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CCGuiaInterna
    fields = '__all__'
  
    
class EnvasesPatioTechadoExtSerializer(serializers.ModelSerializer):
  estado_envase_label = serializers.SerializerMethodField()
  
  class Meta:
    model = EnvasesPatioTechadoExt
    fields = '__all__'
  
  def get_estado_envase_label(self, obj):
    return obj.get_estado_envase_display()
    
class PatioTechadoExteriorSerializer(serializers.ModelSerializer):
  envases = EnvasesPatioTechadoExtSerializer(many=True, read_only=True, source='envasespatiotechadoext_set')
  variedad = serializers.SerializerMethodField()
  control_calidad = serializers.SerializerMethodField()
  estado_lote_label = serializers.SerializerMethodField()
  ubicacion_label = serializers.SerializerMethodField()
  
  class Meta:     
    model = PatioTechadoExterior
    fields = '__all__'
    
  def get_variedad(self, obj):
    try:
      variedad = EnvasesPatioTechadoExt.objects.filter(guia_patio = obj.pk).first().variedad
      if variedad:
        return variedad
      else:
        return None
        
    except:
      return None
    
  def get_control_calidad(self, obj):
    try:
      if obj.tipo_recepcion.model == 'recepcionmp':
        guia = CCGuiaInterna.objects.get(pk = obj.cc_guia.pk).id_guia
        control_calidad = CCRecepcionMateriaPrima.objects.get(pk = guia)
        serializer = CCRecepcionMateriaPrimaSerializer(control_calidad)
        return serializer.data
    except:
      print('An exception occurred')
  
  def get_estado_lote_label(self, obj):
    return obj.get_estado_lote_display()
  
  def get_ubicacion_label(self, obj):
    return obj.get_ubicacion_display()
    