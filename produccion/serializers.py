from .models import *
from rest_framework import serializers


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'
        
class DetalleProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'
        
        
class OperariosEnProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnProduccion
        fields = '__all__'
        
class LotesProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotesPrograma
        fields = '__all__'
        
class TarjaResultanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultante
        fields = '__all__'
    
class ReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reproceso
        fields = '__all__'
        
class OperariosEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperariosEnReproceso
        fields = '__all__'
        
class BinsEnReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinsEnReproceso
        fields = '__all__'
        
class TarjaResultanteReprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjaResultanteReproceso
        fields = '__all__'
        
        