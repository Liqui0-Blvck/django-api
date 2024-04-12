from rest_framework import serializers
from .models import *
from django.contrib.contenttypes.models import *


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
    
  def get_estado_lote_label(self, obj):
    return obj.get_estado_lote_display()
  
  def get_ubicacion_label(self, obj):
    return obj.get_ubicacion_display()
    

    
class BinBodegaSerializer(serializers.ModelSerializer):
  kilos_bin = serializers.SerializerMethodField()
  programa_produccion = serializers.SerializerMethodField()
  
  class Meta:
      model = BinBodega
      fields = '__all__'
      
    
  def get_programa_produccion(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2' or obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.produccion.id
    elif obj.tipo_binbodega.model == 'bodegag1reproceso' or obj.tipo_binbodega.model == 'bodegag2reproceso' or obj.tipo_binbodega.model == 'bodegaresiduosreproceso':
      return obj.binbodega.reproceso.id
    else:
      return obj.pk
    
    
    
  def get_kilos_bin(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2':
      return obj.binbodega.kilos_fruta
    elif obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.kilos_residuo
    else:
      return 0
      

class DetalleBinBodegaSerializer(serializers.ModelSerializer):
  tipo_binbodega_id = serializers.SerializerMethodField(read_only=True)
  tipo_binbodega = serializers.StringRelatedField(read_only=True)
  binbodega = serializers.SerializerMethodField()
  estado_binbodega = serializers.SerializerMethodField()
  kilos_bin = serializers.SerializerMethodField()
  programa_produccion = serializers.SerializerMethodField()
  
  
  def get_programa_produccion(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2' or obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.produccion.produccion.pk
    elif obj.tipo_binbodega.model == 'bodegag1reproceso' or obj.tipo_binbodega.model == 'bodegag2reproceso' or obj.tipo_binbodega.model == 'bodegaresiduosreproceso':
      return obj.binbodega.reproceso.pk
    else:
      return None
    
  
  
  def get_estado_binbodega(self, obj):
      return obj.get_estado_binbodega_display()
  
  def get_binbodega(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2' or obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.produccion.codigo_tarja
    elif obj.tipo_binbodega.model == 'bodegag1reproceso' or obj.tipo_binbodega.model == 'bodegag2reproceso' or obj.tipo_binbodega.model == 'bodegaresiduosreproceso':
      return obj.binbodega.reproceso.codigo_tarja
    else:
      return None
    
    
  def get_kilos_bin(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2':
      return obj.binbodega.kilos_fruta
    elif obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.kilos_residuo
    else:
      return None
    
  def get_tipo_binbodega_id(self, obj):
      # Obtén el ContentType del tipo de bin de la bodega asociado
      try:
          tipo_bin_bodega_content_type = ContentType.objects.get_for_id(obj.tipo_binbodega_id)
          return tipo_bin_bodega_content_type.id
      except ContentType.DoesNotExist:
          return None
      
  class Meta:
      model = BinBodega
      fields = '__all__'
      
      
      
class BodegaG1Serializer(serializers.ModelSerializer):
    class Meta:
      model = BodegaG1
      fields = '__all__'

class BodegaG2Serializer(serializers.ModelSerializer):
    class Meta:
      model = BodegaG2
      fields = '__all__'
      
class BodegaG1ReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
      model = BodegaG1Reproceso
      fields = '__all__'

class BodegaG2ReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
      model = BodegaG2Reproceso
      fields = '__all__'


class BodegaResiduosSerializer(serializers.ModelSerializer):
  class Meta:
    model = BodegaResiduos
    fields = '__all__'