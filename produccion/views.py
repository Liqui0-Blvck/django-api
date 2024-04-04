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
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return OperariosEnProduccionSerializer
        return DetalleOperariosEnProduccionSerializer
    
    def retrieve(self, request, produccion_pk=None, pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = get_object_or_404(self.get_queryset(),produccion=produccion, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def list(self, request, produccion_pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = OperariosEnProduccion.objects.filter(produccion=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class LotesProgramaViewSet(viewsets.ModelViewSet):
    queryset = LotesPrograma.objects.all()
    serializer_class = LotesProgramaSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return LotesProgramaSerializer
        return DetalleLotesProgramaSerializer
    
    def retrieve(self, request, produccion_pk=None, pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = get_object_or_404(self.get_queryset(),produccion=produccion, pk=pk)
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
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return TarjaResultanteSerializer
        return DetalleTarjaResultanteSerializer
    
    def retrieve(self, request, produccion_pk=None, pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = get_object_or_404(self.get_queryset(), produccion=produccion, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def list(self, request, produccion_pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = TarjaResultante.objects.filter(produccion=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ReprocesoViewSet(viewsets.ModelViewSet):
    queryset = Reproceso.objects.all()
    serializer_class = ReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ReprocesoSerializer
        return DetalleReprocesoSerializer
    
    def retrieve(self, request, pk=None, ):
        produccion = get_object_or_404(Reproceso, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, ):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class BinsEnReprocesoViewSet(viewsets.ModelViewSet):
    queryset = BinsEnReproceso.objects.all()
    serializer_class = BinsEnReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return BinsEnReprocesoSerializer
        return DetalleBinsEnReprocesoSerializer
    
    def retrieve(self, request,reproceso_pk=None, pk=None):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        produccion = get_object_or_404(self.get_queryset(),reproceso=reproceso, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, reproceso_pk=None, ):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        queryset = get_list_or_404(BinsEnReproceso, reproceso=reproceso)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class TarjaResultanteReprocesoViewSet(viewsets.ModelViewSet):
    queryset = TarjaResultanteReproceso.objects.all()
    serializer_class = TarjaResultanteReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return TarjaResultanteReprocesoSerializer
        return DetalleTarjaResultanteReprocesoSerializer
    
    def retrieve(self, request,reproceso_pk=None, pk=None):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        produccion = get_object_or_404(self.get_queryset(),reproceso=reproceso, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, reproceso_pk=None):
        produccion = get_object_or_404(Reproceso, pk=reproceso_pk)
        queryset = TarjaResultanteReproceso.objects.filter(reproceso=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OperariosEnReprocesoViewSet(viewsets.ModelViewSet):
    queryset = OperariosEnReproceso.objects.all()
    serializer_class = OperariosEnReprocesoSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return OperariosEnReprocesoSerializer
        return DetalleOperariosEnReprocesoSerializer
    
    def retrieve(self, request,reproceso_pk=None, pk=None):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        produccion = get_object_or_404(self.get_queryset(),reproceso=reproceso, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, reproceso_pk=None):
        produccion = get_object_or_404(Reproceso, pk=reproceso_pk)
        queryset = OperariosEnReproceso.objects.filter(reproceso=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





