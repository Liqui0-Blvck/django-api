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
  permission_classes = [IsAuthenticated,]
  
class PatioTechadoExteriorUpdatedViewset(viewsets.ModelViewSet):
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  permission_classes = [IsAuthenticated,]
  
  

class PatioTechadoExteriorViewset(viewsets.ModelViewSet):
  # search_fields = ['id_recepcion']
  # filter_backends = (filters.SearchFilter, )
  lookup_field = 'id_recepcion'
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  permission_classes = [IsAuthenticated,]

  

class EnvasesPatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = EnvasesPatioTechadoExt.objects.all()
  serializer_class = EnvasesPatioTechadoExtSerializer
  permission_classes = [IsAuthenticated,]
