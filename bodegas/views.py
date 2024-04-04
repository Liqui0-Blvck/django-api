from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_list_or_404, get_object_or_404

class PatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = PatioTechadoExterior.objects.all()
  serializer_class = PatioTechadoExteriorSerializer
  permission_classes = [IsAuthenticated,]
  
  def retrieve(self, request, pk=None):
    guiapatio = get_object_or_404(PatioTechadoExterior, pk=pk)
    serializer = self.get_serializer(guiapatio)
    return Response(serializer.data)

  def list(self, request, guia_patio_pk=None):
    queryset = self.get_queryset()
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)


class EnvasesPatioTechadoExteriorViewset(viewsets.ModelViewSet):
  queryset = EnvasesPatioTechadoExt.objects.all()
  serializer_class = EnvasesPatioTechadoExtSerializer
  permission_classes = [IsAuthenticated,]

  def retrieve(self, request, guia_patio_pk=None, pk=None):
    guiapatio = get_object_or_404(PatioTechadoExterior, pk=guia_patio_pk)
    queryset = get_object_or_404(self.get_queryset(),guia_patio=guiapatio, pk=pk)
    serializer = self.get_serializer(queryset)
    return Response(serializer.data)

  def list(self, request, guia_patio_pk=None):
    guiapatio = get_object_or_404(PatioTechadoExterior, pk=guia_patio_pk)
    queryset = get_list_or_404(self.get_queryset(), guia_patio=guiapatio)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)


class BinBodegaViewSet(viewsets.ModelViewSet):
    queryset = BinBodega.objects.all()
    serializer_class = BinBodegaSerializer
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return BinBodegaSerializer
        return DetalleBinBodegaSerializer