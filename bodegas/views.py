from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *



class CCGuiaInternaViewset(viewsets.ModelViewSet):
  queryset = CCGuiaInterna.objects.all()
  serializer_class = CCGuiaInternaSerializer
  
class PatioTechadoExteriorUpdatedViewset(viewsets.ModelViewSet):
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  
  

class PatioTechadoExteriorViewset(viewsets.ModelViewSet):
  # search_fields = ['id_recepcion']
  # filter_backends = (filters.SearchFilter, )
  lookup_field = 'id_recepcion'
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer

  

class EnvasesPatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = EnvasesPatioTechadoExt.objects.all()
  serializer_class = EnvasesPatioTechadoExtSerializer
