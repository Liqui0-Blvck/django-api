from rest_framework import serializers
from .models import *


class CCGuiaInternaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CCGuiaInterna
    fields = '__all__'
    
class EnvasesPatioTechadoExtSerializer(serializers.ModelSerializer):
  class Meta:
    model = EnvasesPatioTechadoExt
    fields = '__all__'
    
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
    

    
class BinBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinBodega
        fields = '__all__'

class DetalleBinBodegaSerializer(serializers.ModelSerializer):
  tipo_binbodega = serializers.StringRelatedField(read_only=True)
  binbodega = serializers.SerializerMethodField()
  estado_binbodega = serializers.SerializerMethodField()
  
  def get_estado_binbodega(self, obj):
      return obj.get_estado_binbodega_display()
  
  def get_binbodega(self, obj):
    if obj.tipo_binbodega.model == 'bodegag1' or obj.tipo_binbodega.model == 'bodegag2' or obj.tipo_binbodega.model == 'bodegaresiduos':
      return obj.binbodega.produccion.codigo_tarja
    elif obj.tipo_binbodega.model == 'bodegag1reproceso' or obj.tipo_binbodega.model == 'bodegag2reproceso' or obj.tipo_binbodega.model == 'bodegaresiduosreproceso':
      return obj.binbodega.reproceso.codigo_tarja
      
      
  class Meta:
      model = BinBodega
      fields = '__all__'
      