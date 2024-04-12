from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CargoPerfilSerializer(serializers.ModelSerializer):
    cargo_label = serializers.SerializerMethodField()
    class Meta:
        model = CargoPerfil
        fields = '__all__'
        
    def get_cargo_label(self, obj):
        return obj.get_cargo_display()




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username']


class OperarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operario
        fields = '__all__'  


class ColosoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coloso
        fields = '__all__'
        

class TractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tractor
        fields = '__all__'


class TractorColosoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractorColoso
        fields = '__all__'


class EtiquetasZplSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetasZpl
        fields = '__all__'




class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cargos = CargoPerfilSerializer(many=True, read_only=True, source='cargoperfil_set')
    class Meta:
        model = Perfil
        fields = '__all__'



class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'


class PersonalizacionPerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta: 
        model = PersonalizacionPerfil
        fields = '__all__'