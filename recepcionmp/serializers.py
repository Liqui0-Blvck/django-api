from rest_framework import serializers
from .models import *
from core.models import *

class EnvasesGuiaRecepcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvasesGuiaRecepcionMp
        fields = '__all__'
        
class RecepcionMpSerializer(serializers.ModelSerializer):
    envases = EnvasesGuiaRecepcionSerializer(many=True, read_only=True, source='envasesguiarecepcionmp_set')
    class Meta:
        model = RecepcionMp
        fields = '__all__'

class GuiaRecepcionMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaRecepcionMP
        fields = '__all__'

class DetalleGuiaRecepcionMPSerializer(serializers.ModelSerializer):
    lotesrecepcionmp =RecepcionMpSerializer(many=True, read_only=True, source='recepcionmp_set')
    nombre_camion = serializers.SerializerMethodField()
    nombre_camionero = serializers.SerializerMethodField()
    estado_recepcion = serializers.SerializerMethodField()
    nombre_productor = serializers.SerializerMethodField()
    nombre_comercializador = serializers.SerializerMethodField()
    nombre_creado_por = serializers.SerializerMethodField()
    
    def get_nombre_creado_por(self, obj):
        if obj.creado_por:
            return "%s %s"% (obj.creado_por.first_name, obj.creado_por.last_name)
    
    def get_nombre_comercializador(self, obj):
        if obj.comercializador:
            return obj.comercializador.nombre
        else:
            return str('Sin comercializador')
    
    def get_nombre_productor(self, obj):
        return obj.productor.nombre
    
    def get_estado_recepcion(self, obj):
        return obj.get_estado_recepcion_display()
    
    def get_nombre_camionero(self, obj):
        chofer = Chofer.objects.get(pk=obj.camionero.pk)
        return "%s %s"% (chofer.nombre, chofer.apellido)
    
    def get_nombre_camion(self, obj):
        return  Camion.objects.get(pk=obj.camion.pk).patente
    
    class Meta:
        model = GuiaRecepcionMP
        fields = '__all__'



class EnvasesGuiaRecepcionMpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvasesGuiaRecepcionMp
        fields = ['envase', 'variedad', 'tipo_producto', 'cantidad_envases']



class DetalleRecepcionMpSerializer(serializers.ModelSerializer):
    envases = EnvasesGuiaRecepcionMpSerializer(many=True, read_only=True, source='envasesguiarecepcionmp_set')
    
    class Meta:
        model = RecepcionMp
        fields = '__all__'
        

class EnvasesMpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvasesMp
        fields = '__all__'
        
        
class EstadoRecepcionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionMp
        fields = ['estado_recepcion']
        



