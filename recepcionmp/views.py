from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import *
import json


class GuiaRecepcionMPViewSet(viewsets.ModelViewSet):
    queryset = GuiaRecepcionMP.objects.all()
    #serializer_class = GuiaRecepcionMPSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    # permission_classes = [IsAuthenticated, ]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return GuiaRecepcionMPSerializer
        return DetalleGuiaRecepcionMPSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RecepcionMpViewSet(viewsets.ModelViewSet):
    queryset = RecepcionMp.objects.all()
    #serializer_class = RecepcionMpSerializer
    # permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RecepcionMpSerializer
        return DetalleRecepcionMpSerializer
    
    def retrieve(self, request, recepcionmp_pk=None, pk=None):
        guiarecepcion = GuiaRecepcionMP.objects.get(pk=recepcionmp_pk)
        queryset = RecepcionMp.objects.get(guiarecepcion=guiarecepcion, pk=pk)
        serializer = RecepcionMpSerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request, recepcionmp_pk=None, *args, **kwargs):
        lotes_request = request.data.get('lotes', '[]')
        lotes = json.loads(lotes_request)
        for lote in lotes:
            serializer = self.get_serializer(data=lote)
            if serializer.is_valid():
                serializer.save()
            envases_request = request.data.get('envases', '[]')
            envases = json.loads(envases_request)
            for envase in envases:
                serializador_envases = EnvasesGuiaRecepcionMpSerializer(data=envase)
                if serializador_envases.is_valid():
                    serializador_envases.save(recepcionmp = serializer.instance)
        guiarecepcion = GuiaRecepcionMP.objects.get(pk=recepcionmp_pk)
        serializer.save(guiarecepcion=guiarecepcion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, recepcionmp_pk=None):
        queryset = self.queryset.filter(guiarecepcion=recepcionmp_pk)
        serializer = DetalleRecepcionMpSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class EnvasesMpViewSet(viewsets.ModelViewSet):

    queryset = EnvasesMp.objects.all()
    serializer_class = EnvasesMpSerializer
    # permission_classes = [IsAuthenticated, ]

class EnvasesGuiaMPViewSet(viewsets.ModelViewSet):
    queryset = EnvasesGuiaRecepcionMp.objects.all()
    serializer_class = EnvasesGuiaRecepcionSerializer