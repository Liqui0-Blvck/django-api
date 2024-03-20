from rest_framework import serializers
from .models import *



class CCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = '__all__'


class DetalleCCRecepcionMateriaPrimaSerializer(serializers.ModelSerializer):
    estado_aprobacion_cc = serializers.SerializerMethodField()
    estado_cc = serializers.SerializerMethodField()
    presencia_insectos_selected = serializers.SerializerMethodField()
    
    def get_presencia_insectos_selected(self, obj):
        if obj.presencia_insectos:
            return  "Si"
        else:
            return "No"
    
    def get_estado_cc(self, obj):
        return obj.get_estado_cc_display()
        
    
    def get_estado_aprobacion_cc(self, obj):
        return obj.get_estado_aprobacion_cc_display()
        
    class Meta:
        model = CCRecepcionMateriaPrima
        fields = '__all__'
        
        
class CCRendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCRendimiento
        fields = '__all__'
        
class CCPepaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCPepa
        fields = '__all__'
        
        

