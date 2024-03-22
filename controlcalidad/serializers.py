from rest_framework import serializers
from .models import *
from recepcionmp.models import *



class CCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = '__all__'
        
class FotosCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotosCC
        fields = '__all__'


class DetalleCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    estado_aprobacion_cc = serializers.SerializerMethodField()
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
    
    def get_productor(self, obj):
        lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
        productor = GuiaRecepcionMP.objects.get(pk = lote.pk).productor.pk
        return productor
    
    def get_guia_recepcion(self, obj):
        lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
        return GuiaRecepcionMP.objects.get(pk = lote.pk).pk
        
    def get_estado_guia(self, obj):
        lote = RecepcionMp.objects.get(pk = obj.recepcionmp.pk).guiarecepcion
        return GuiaRecepcionMP.objects.get(pk = lote.pk).estado_recepcion
        
    
    def get_estado_aprobacion_cc(self, obj):
        return obj.get_estado_aprobacion_cc_display()
    
    def get_numero_lote(self, obj):
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
        
        
class CCRendimientoSerializer(serializers.ModelSerializer):
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
        
class CCPepaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCPepa
        fields = '__all__'
        
        

