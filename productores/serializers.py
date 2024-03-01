from rest_framework import serializers
from .models import *



class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields = '__all__'


