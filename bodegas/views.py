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
  

class PatioTechadoExteriorViewset(viewsets.ModelViewSet):
  search_fields = ['id_recepcion']
  filter_backends = (filters.SearchFilter, )
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    req_data = request.data
    print(instance)
    print(req_data)
    return super().update(request, *args, **kwargs)
  

class EnvasesPatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = EnvasesPatioTechadoExt.objects.all()
  serializer_class = EnvasesPatioTechadoExtSerializer
