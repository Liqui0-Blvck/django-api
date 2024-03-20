from rest_framework import serializers
from .models import *


class CCGuiaInternaSerializer(serializers.ModelSerializer):
  class Meta:
    model = CCGuiaInterna
    fields = '__all__'
    
class PatioTechadoExteriorSerializer(serializers.ModelSerializer):
  class Meta:
    model = PatioTechadoExterior
    fields = '__all__'
    
class EnvasesPatioTechadoExtSerializer(serializers.ModelSerializer):
  class Meta:
    model = EnvasesPatioTechadoExt
    fields = '__all__'
    