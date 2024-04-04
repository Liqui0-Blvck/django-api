from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ProduccionSerializer
        return DetalleProduccionSerializer
    
    def retrieve(self, request, pk=None, ):
        produccion = get_object_or_404(Produccion, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, ):
        queryset = get_list_or_404(Produccion,)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OperariosEnProduccionViewSet(viewsets.ModelViewSet):
    queryset = OperariosEnProduccion.objects.all()
    serializer_class = OperariosEnProduccionSerializer
    permission_classes = [IsAuthenticated,]

class LotesProgramaViewSet(viewsets.ModelViewSet):
    queryset = LotesPrograma.objects.all()
    serializer_class = LotesProgramaSerializer
    permission_classes = [IsAuthenticated,]
    
    # def get_serializer_class(self):        
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return RecepcionMpSerializer
    #     return DetalleRecepcionMpSerializer
    
    def retrieve(self, request, produccion_pk=None, pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = get_object_or_404(produccion=produccion, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def list(self, request, produccion_pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = LotesPrograma.objects.filter(produccion=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TarjaResultanteViewSet(viewsets.ModelViewSet):
    queryset = TarjaResultante.objects.all()
    serializer_class = TarjaResultanteSerializer
    permission_classes = [IsAuthenticated,]

class ReprocesoViewSet(viewsets.ModelViewSet):
    queryset = Reproceso.objects.all()
    serializer_class = ReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
class OperariosEnReprocesoViewSet(viewsets.ModelViewSet):
    queryset = OperariosEnReproceso.objects.all()
    serializer_class = OperariosEnReprocesoSerializer
    permission_classes = [IsAuthenticated,]

class BinsEnReprocesoViewSet(viewsets.ModelViewSet):
    queryset = BinsEnReproceso.objects.all()
    serializer_class = BinsEnReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
class TarjaResultanteReprocesoViewSet(viewsets.ModelViewSet):
    queryset = TarjaResultanteReproceso.objects.all()
    serializer_class = TarjaResultanteReprocesoSerializer
    permission_classes = [IsAuthenticated,]





