from .models import *
from rest_framework import serializers
from recepcionmp.models import *
from bodegas.models import *


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
        
class DetalleLotesProgramaSerializer(serializers.ModelSerializer):
    numero_lote = serializers.SerializerMethodField()
    guia_patio = serializers.SerializerMethodField()
    numero_bin = serializers.SerializerMethodField()
    kilos_fruta = serializers.SerializerMethodField()
    variedad = serializers.SerializerMethodField()
    guia_recepcion = serializers.SerializerMethodField()
    control_calidad = serializers.SerializerMethodField()
    
    
    
    class Meta:
        model = LotesPrograma
        fields = '__all__'
        
    def get_control_calidad(self, obj):
        if obj.bodega_techado_ext.guia_patio.tipo_recepcion.model == 'recepcionmp':
            recepcion = RecepcionMp.objects.filter(pk = obj.bodega_techado_ext.guia_patio.id_recepcion).first().pk
            return recepcion
        else:
            return None
        
    def get_numero_lote(self, obj):
        if obj.bodega_techado_ext.guia_patio.tipo_recepcion.model == 'recepcionmp':
            recepcion = RecepcionMp.objects.filter(pk = obj.bodega_techado_ext.guia_patio.id_recepcion).first().numero_lote
            return recepcion
        else:
            return None
    
    def get_guia_patio(self, obj):
        patio_techado_ext = EnvasesPatioTechadoExt.objects.filter(pk=obj.bodega_techado_ext.pk).first()
        if patio_techado_ext:
            return patio_techado_ext.guia_patio.id_recepcion    
        else:
            return None
        
    def get_numero_bin(self, obj):
        patio_techado_ext = EnvasesPatioTechadoExt.objects.filter(pk=obj.bodega_techado_ext.pk).first()
        if patio_techado_ext:
            return patio_techado_ext.numero_bin
        else:
            return None 
        
    def get_kilos_fruta (self, obj):
        patio_techado_ext = EnvasesPatioTechadoExt.objects.filter(pk=obj.bodega_techado_ext.pk).first()
        if patio_techado_ext:
            return patio_techado_ext.kilos_fruta
        else:
            return None 
    def get_variedad(self, obj):
        patio_techado_ext = EnvasesPatioTechadoExt.objects.filter(pk=obj.bodega_techado_ext.pk).first()
        if patio_techado_ext:
            return patio_techado_ext.variedad
        else:
            return None   
        
    def get_guia_recepcion(self, obj):
        if obj.bodega_techado_ext.guia_patio.tipo_recepcion.model == 'recepcionmp':
            recepcion = RecepcionMp.objects.filter(pk = obj.bodega_techado_ext.guia_patio.id_recepcion).first().guiarecepcion.pk    
            return recepcion
        else:
            return None
        
        
class OperariosEnProduccionSerializer(serializers.ModelSerializer):
    nombres = serializers.SerializerMethodField()
    rut_operario = serializers.SerializerMethodField()
    tipo_operario = serializers.SerializerMethodField()
    
    
    class Meta:
        model = OperariosEnProduccion
        fields = '__all__'
        
    def get_tipo_operario(self, obj):
        return obj.operario.get_tipo_operario_display()
        
    def get_rut_operario(self, obj):
        return obj.operario.rut
    
    def get_nombres(self, obj):
        return f'{obj.operario.nombre} {obj.operario.apellido}'
        
        
        
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
    estado_label = serializers.SerializerMethodField()
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
    
    def get_estado_label(self, obj):
        return obj.get_estado_display()
    class Meta:
        model = Reproceso
        fields = '__all__'
        
class OperariosEnReprocesoSerializer(serializers.ModelSerializer):
    nombres = serializers.SerializerMethodField()
    rut_operario = serializers.SerializerMethodField()
    tipo_operario = serializers.SerializerMethodField()
    
    class Meta:
        model = OperariosEnReproceso
        fields = '__all__'
        
    def get_tipo_operario(self, obj):
        return obj.operario.get_tipo_operario_display()
        
    def get_rut_operario(self, obj):
        return obj.operario.rut
    
    def get_nombres(self, obj):
        return f'{obj.operario.nombre} {obj.operario.apellido}'
        
class DetalleOperariosEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnReproceso
        fields = '__all__'
        
class BinsEnReprocesoSerializer(serializers.ModelSerializer):
    programa_produccion = serializers.SerializerMethodField()

    class Meta:
        model = BinsEnReproceso
        fields = '__all__'
    
    def get_programa_produccion(self, obj):
        if obj.tipo_bin_bodega.model == 'bodegag1' or obj.tipo_bin_bodega.model == 'bodegag2' or obj.tipo_bin_bodega.model == 'bodegaresiduos':
            return obj.bin_bodega.produccion.produccion.id
        elif obj.tipo_bin_bodega.model == 'bodegag1reproceso' or obj.tipo_bin_bodega.model == 'bodegag2reproceso' or obj.tipo_bin_bodega.model == 'bodegaresiduosreproceso':
            return obj.bin_bodega.reproceso.reproceso.id
        else:
            return obj.pk
        
        
    
     
        
        
class DetalleBinsEnReprocesoSerializer(serializers.ModelSerializer):
    programa_produccion = serializers.SerializerMethodField()
    kilos_bin = serializers.SerializerMethodField()
    identificador_bin_bodega = serializers.SerializerMethodField()
    
    class Meta:
        model = BinsEnReproceso
        fields = '__all__'
        
    def get_identificador_bin_bodega(self, obj):
        if obj.tipo_bin_bodega.model == 'bodegag1' or obj.tipo_bin_bodega.model == 'bodegag2' or obj.tipo_bin_bodega.model == 'bodegaresiduos':
            return obj.bin_bodega.produccion.id
        elif obj.tipo_bin_bodega.model == 'bodegag1reproceso' or obj.tipo_bin_bodega.model == 'bodegag2reproceso' or obj.tipo_bin_bodega.model == 'bodegaresiduosreproceso':
            return obj.bin_bodega.reproceso.id
        else:
            return obj.pk
        
    def get_kilos_bin(self, obj):
        if obj.tipo_bin_bodega.model == 'bodegag1' or obj.tipo_bin_bodega.model == 'bodegag2':
            return obj.bin_bodega.kilos_fruta
        elif obj.tipo_bin_bodega.model == 'bodegaresiduos':
            return obj.bin_bodega.kilos_residuo
        else:
            return 0
        
    def get_programa_produccion(self, obj):
        if obj.tipo_bin_bodega.model == 'bodegag1' or obj.tipo_bin_bodega.model == 'bodegag2':
            return obj.bin_bodega.produccion.produccion.pk
        
        elif obj.tipo_bin_bodega.model == 'bodegag1reproceso' or obj.tipo_bin_bodega.model == 'bodegag2reproceso':
            return obj.bin_bodega.reproceso.reproceso.pk

        
        
class TarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultanteReproceso
        fields = '__all__'
        
class DetalleTarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultanteReproceso
        fields = '__all__'
        
         
        