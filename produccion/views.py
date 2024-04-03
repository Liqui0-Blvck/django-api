from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer
    permission_classes = [IsAuthenticated,]

class OperariosEnProduccionViewSet(viewsets.ModelViewSet):
    queryset = OperariosEnProduccion.objects.all()
    serializer_class = OperariosEnProduccionSerializer
    permission_classes = [IsAuthenticated,]

class LotesProgramaViewSet(viewsets.ModelViewSet):
    queryset = LotesPrograma.objects.all()
    serializer_class = LotesProgramaSerializer
    permission_classes = [IsAuthenticated,]

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





