from rest_framework import serializers
from .models import *
from core.models import *

class RecepcionMpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecepcionMp
        fields = '__all__'

class GuiaRecepcionMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaRecepcionMP
        fields = '__all__'

class DetalleGuiaRecepcionMPSerializer(serializers.ModelSerializer):
    lotesrecepcionmp =RecepcionMpSerializer(many=True, read_only=True, source='recepcionmp_set')
    camion = serializers.SerializerMethodField()
    camionero = serializers.SerializerMethodField()
    estado_recepcion = serializers.SerializerMethodField()
    productor = serializers.SerializerMethodField()
    comercializador = serializers.SerializerMethodField()
    creado_por = serializers.SerializerMethodField()
    
    def get_creado_por(self, obj):
        if obj.creado_por:
            return "%s %s"% (obj.creado_por.first_name, obj.creado_por.last_name)
    
    def get_comercializador(self, obj):
        if obj.comercializador:
            return obj.comercializador.nombre
        else:
            return str('Sin comercializador')
    
    def get_productor(self, obj):
        return obj.productor.nombre
    
    def get_estado_recepcion(self, obj):
        return obj.get_estado_recepcion_display()
    
    def get_camionero(self, obj):
        chofer = Chofer.objects.get(pk=obj.camionero.pk)
        return "%s %s"% (chofer.nombre, chofer.apellido)
    
    def get_camion(self, obj):
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
        



