from .models import *
from rest_framework import serializers
from recepcionmp.models import *


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'
        
class DetalleProduccionSerializer(serializers.ModelSerializer):
    lotes = serializers.SerializerMethodField()
    operarios = serializers.SerializerMethodField()
    tarjas_resultantes = serializers.SerializerMethodField()
    estado_label = serializers.SerializerMethodField()
    
    
    def get_tarjas_resultantes(self, obj):
        tarjas = TarjaResultante.objects.filter(produccion=obj.pk)
        return TarjaResultanteSerializer(tarjas, many=True).data
    
    def get_operarios(self, obj):
        operarios = OperariosEnProduccion.objects.filter(produccion=obj.pk)
        return OperariosEnProduccionSerializer(operarios, many=True).data
    
    def get_lotes(self, obj):
        lotes = LotesPrograma.objects.filter(produccion=obj.pk)
        return LotesProgramaSerializer(lotes, many=True).data
    
    def get_estado_label(self, obj):
        return obj.get_estado_display()
    
    class Meta:
        model = Produccion
        fields = '__all__'


class LotesProgramaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LotesPrograma
        fields = '__all__'
        
class DetalleLotesProgramaSerializer(serializers.ModelSerializer):
    numero_lote = serializers.SerializerMethodField()
    class Meta:
        model = LotesPrograma
        fields = '__all__'
        
    def get_numero_lote(self, obj):
        if obj.bodega_techado_ext.guia_patio.tipo_recepcion.model == 'recepcionmp':
            recepcion = RecepcionMp.objects.filter(pk = obj.bodega_techado_ext.guia_patio.id_recepcion).first().numero_lote
            return recepcion
        else:
            return None
        
class OperariosEnProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnProduccion
        fields = '__all__'
        
class DetalleOperariosEnProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnProduccion
        fields = '__all__'
        
class TarjaResultanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultante
        fields = '__all__'
        
class DetalleTarjaResultanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultante
        fields = '__all__'
    
class ReprocesoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Reproceso
        fields = '__all__'
        
class DetalleReprocesoSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()
    bins = serializers.SerializerMethodField()
    operarios = serializers.SerializerMethodField()
    tarjas_resultantes = serializers.SerializerMethodField()
    
    def get_tarjas_resultantes(self, obj):
        tarjas = TarjaResultanteReproceso.objects.filter(reproceso=obj.pk)
        return TarjaResultanteReprocesoSerializer(tarjas, many=True).data
    
    def get_operarios(self, obj):
        operarios = OperariosEnReproceso.objects.filter(reproceso=obj.pk)
        return OperariosEnReprocesoSerializer(operarios, many=True).data
    
    def get_bins(self, obj):
        bins = BinsEnReproceso.objects.filter(reproceso=obj.pk)
        return BinsEnReprocesoSerializer(bins, many=True).data
    
    def get_estado(self, obj):
        return obj.get_estado_display()
    class Meta:
        model = Reproceso
        fields = '__all__'
        
class OperariosEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnReproceso
        fields = '__all__'
        
class DetalleOperariosEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnReproceso
        fields = '__all__'
        
class BinsEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinsEnReproceso
        fields = '__all__'
        
class DetalleBinsEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinsEnReproceso
        fields = '__all__'
        
class TarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultanteReproceso
        fields = '__all__'
        
class DetalleTarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultanteReproceso
        fields = '__all__'
        
         
        