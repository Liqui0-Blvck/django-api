from rest_framework import serializers
from .models import *



class GuiaRecepcionMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaRecepcionMP
        fields = '__all__'



class RecepcionMpSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecepcionMp
        fields = '__all__'


