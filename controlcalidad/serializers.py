from rest_framework import serializers
from .models import *
from recepcionmp.models import *



# class CCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CCRecepcionMateriaPrima
#         fields = '__all__'
        
# class FotosCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FotosCC
#         fields = '__all__'


# class DetalleCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
#     estado_aprobacion_cc = serializers.SerializerMethodField()
#     estado_cc_label = serializers.SerializerMethodField()
#     numero_lote = serializers.SerializerMethodField()
#     presencia_insectos_selected = serializers.SerializerMethodField()
#     productor = serializers.SerializerMethodField()
#     guia_recepcion = serializers.SerializerMethodField()
#     estado_guia = serializers.SerializerMethodField()
#     fotos_cc = FotosCCRecepcionMateriaPrimaSerializer(many=True, read_only=True, source='fotoscc_set')
    
#     def get_presencia_insectos_selected(self, obj):
#         if obj.presencia_insectos:
#             return  "Si"
#         else:
#             return "No"
    
#     def get_estado_cc_label(self, obj):
#         return obj.get_estado_cc_display()
    
#     def get_productor(self, obj):
#         lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
#         productor = GuiaRecepcionMP.objects.get(pk = lote.pk).productor.pk
#         return productor
    
#     def get_guia_recepcion(self, obj):
#         lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
#         return GuiaRecepcionMP.objects.get(pk = lote.pk).pk
        
#     def get_estado_guia(self, obj):
#         lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
#         return GuiaRecepcionMP.objects.get(pk = lote.pk).estado_recepcion
        
    
#     def get_estado_aprobacion_cc(self, obj):
#         return obj.get_estado_aprobacion_cc_display()
    
#     def get_numero_lote(self, obj):
#         try:
#             numero_lote_aprobado = RecepcionMp.objects.get(id=obj.recepcionmp.id).numero_lote
#             if numero_lote_aprobado:
#                 return numero_lote_aprobado
#             else:
#                 return LoteRecepcionMpRechazadoPorCC.objects.get(recepcionmp=obj.recepcionmp).numero_lote_rechazado
#         except RecepcionMp.DoesNotExist:
#             pass
        
#     class Meta:
#         model = CCRecepcionMateriaPrima
#         fields = '__all__'
        
        
# class CCRendimientoSerializer(serializers.ModelSerializer):
#     cc_recepcionmp = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = CCRendimiento
#         fields = '__all__'
#         extra_kwargs = {
#             "cc_recepcionmp": {"required": False, "allow_null": False},
#         }
        
# class CCPepaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CCPepa
#         fields = '__all__'
        
        
class CCTarjaResultanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTarjaResultante
        fields = '__all__'

class CCTarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTarjaResultanteReproceso
        fields = '__all__'
        
        
        
class CCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = '__all__'
        
class FotosCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotosCC
        fields = '__all__'

class CCPepaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCPepa
        fields = '__all__'
        
class CCRendimientoSerializer(serializers.ModelSerializer):
    cc_rendimiento = CCPepaSerializer(read_only=True, source='cdcpepa')
    cc_recepcionmp = serializers.PrimaryKeyRelatedField(read_only=True)
    cc_ok = serializers.SerializerMethodField()
    cc_calibrespepaok = serializers.SerializerMethodField()
    class Meta:
        model = CCRendimiento
        fields = '__all__'
        extra_kwargs = {    
            "cc_recepcionmp": {"required": False, "allow_null": False},
        }
    
    def get_cc_ok(self, obj):
        try:
            return CCPepa.objects.get(cc_rendimiento = obj.pk, cc_pepaok = True).cc_pepaok
        except: 
            return 'Sin Control Pepa Registrado'
        
    def get_cc_calibrespepaok(self, obj):
        try:
            return CCPepa.objects.get(cc_rendimiento = obj.pk, cc_calibrespepaok = True).cc_pepaok
        except: 
            return False
        


class DetalleCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    control_rendimiento =CCRendimientoSerializer(read_only=True, many=True, source='ccrendimiento_set')
    estado_aprobacion_cc_label = serializers.SerializerMethodField()
    estado_cc_label = serializers.SerializerMethodField()
    numero_lote = serializers.SerializerMethodField()
    presencia_insectos_selected = serializers.SerializerMethodField()
    productor = serializers.SerializerMethodField()
    guia_recepcion = serializers.SerializerMethodField()
    estado_guia = serializers.SerializerMethodField()
    fotos_cc = FotosCCRecepcionMateriaPrimaSerializer(many=True, read_only=True, source='fotoscc_set')
    
    def get_presencia_insectos_selected(self, obj):
        if obj.presencia_insectos:
            return  "Si"
        else:
            return "No"
    
    def get_estado_cc_label(self, obj):
        return obj.get_estado_cc_display()
    
    # def get_productor(self, obj):
    #     lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
    #     productor = GuiaRecepcionMP.objects.get(pk = lote.pk).productor.pk
    #     return productor
    
    def get_productor(self, obj):
        return obj.recepcionmp.guiarecepcion.productor.nombre
    
    def get_guia_recepcion(self, obj):
        return obj.recepcionmp.guiarecepcion.pk
        
    def get_estado_guia(self, obj):
        return obj.recepcionmp.guiarecepcion.estado_recepcion
        
    
    def get_estado_aprobacion_cc_label(self, obj):
        return obj.get_estado_aprobacion_cc_display()
    
    def get_numero_lote(self, obj):
    #     if obj.recepcionmp.estado_recepcion <= '3':
    #         return obj.recepcionmp.numero_lote
    #     elif obj.recepcionmp.estado_recepcion == '4':
    #         rechazo = LoteRecepcionMpRechazadoPorCC.objects.filter(recepcionmp = obj.recepcionmp.pk)
    #         return rechazo.numero_lote_rechazado 
        try:
            numero_lote_aprobado = RecepcionMp.objects.get(id=obj.recepcionmp.id).numero_lote
            if numero_lote_aprobado:
                return numero_lote_aprobado
            else:
                return LoteRecepcionMpRechazadoPorCC.objects.get(recepcionmp=obj.recepcionmp).numero_lote_rechazado
        except RecepcionMp.DoesNotExist:
            pass
        
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = '__all__'
        

class MuestraSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    basura = serializers.FloatField()
    pelon = serializers.FloatField()
    ciega = serializers.FloatField()
    cascara = serializers.FloatField()
    pepa_huerto = serializers.FloatField()
    pepa_bruta = serializers.FloatField()
    
    
class CCPepaMuestraSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    mezcla = serializers.FloatField()
    insecto = serializers.FloatField()
    hongo = serializers.FloatField()
    dobles = serializers.FloatField()
    color = serializers.FloatField()
    vana = serializers.FloatField()
    pgoma = serializers.FloatField()
    goma = serializers.FloatField()
    
class CalibresSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    precalibre = serializers.FloatField()
    calibre_18_20 = serializers.FloatField()
    calibre_20_22 = serializers.FloatField()
    calibre_23_25 = serializers.FloatField()
    calibre_25_27 = serializers.FloatField()
    calibre_27_30 = serializers.FloatField()
    calibre_30_32 = serializers.FloatField()
    calibre_32_34 = serializers.FloatField()
    calibre_34_36 = serializers.FloatField()
    calibre_36_40 = serializers.FloatField()
    calibre_40_mas = serializers.FloatField()
    

class DescuentosSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    pepa_exp = serializers.FloatField()
    cat2 = serializers.FloatField()
    desechos = serializers.FloatField()
    mezcla = serializers.FloatField()
    color = serializers.FloatField()
    dobles = serializers.FloatField()
    insecto = serializers.FloatField()
    hongo = serializers.FloatField()
    vana = serializers.FloatField()
    pgoma = serializers.FloatField()
    goma = serializers.FloatField()
    
class AportePexSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    exportable = serializers.FloatField()
    cat2 = serializers.FloatField()
    des = serializers.FloatField()
    

class PorcentajeLiquidarSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    exportable = serializers.FloatField()
    cat2 = serializers.FloatField()
    des = serializers.FloatField()
        
class KilosMermaSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    exportable = serializers.FloatField()
    cat2 = serializers.FloatField()
    des = serializers.FloatField()
    
class MermaPorcentajeSerializer(serializers.Serializer):
    cc_lote = serializers.IntegerField()
    exportable = serializers.FloatField()
    cat2 = serializers.FloatField()
    des = serializers.FloatField()
    
class CalculoFinalSerializer(serializers.Serializer):
    kilos_netos = serializers.FloatField()
    kilos_brutos = serializers.FloatField()
    por_brutos = serializers.FloatField()
    merma_exp = serializers.FloatField()
    final_exp = serializers.FloatField()
    merma_cat2 = serializers.FloatField()
    final_cat2 = serializers.FloatField()
    merma_des = serializers.FloatField()
    final_des = serializers.FloatField()
    
    
class EstadoAprobacionJefaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = ['estado_aprobacion_cc']
        
class EstadoContraMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRecepcionMateriaPrima 
        fields = ['esta_contramuestra']