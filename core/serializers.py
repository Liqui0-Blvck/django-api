from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        # fields = '__all__'    
