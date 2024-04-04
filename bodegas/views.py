from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import datetime



class CCGuiaInternaViewset(viewsets.ModelViewSet):
  queryset = CCGuiaInterna.objects.all()
  serializer_class = CCGuiaInternaSerializer
  
class PatioTechadoExteriorUpdatedViewset(viewsets.ModelViewSet):
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  
  

class PatioTechadoExteriorViewset(viewsets.ModelViewSet):
  lookup_field = 'id_recepcion'
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer

  

class EnvasesPatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = EnvasesPatioTechadoExt.objects.all()
  serializer_class = EnvasesPatioTechadoExtSerializer

