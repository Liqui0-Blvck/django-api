from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status


class GuiaRecepcionMPViewSet(viewsets.ModelViewSet):
    queryset = GuiaRecepcionMP.objects.all()
    #serializer_class = GuiaRecepcionMPSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated, ]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return GuiaRecepcionMPSerializer
        return DetalleGuiaRecepcionMPSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creado_por=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RecepcionMpViewSet(viewsets.ModelViewSet):
    queryset = RecepcionMp.objects.all()
    #serializer_class = RecepcionMpSerializer
    permission_classes = [IsAuthenticated, ]
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
        serializer = self.get_serializer(data=request.data)
        envases = request.data['envases']
        serializador_envases = EnvasesGuiaRecepcionMpSerializer(data=envases, many=True)
        serializer.is_valid(raise_exception=True)
        guiarecepcion = GuiaRecepcionMP.objects.get(pk=recepcionmp_pk)
        serializer.save(guiarecepcion=guiarecepcion)
        serializador_envases.is_valid(raise_exception=True)        
        serializador_envases.save(recepcionmp=serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, recepcionmp_pk=None):
        queryset = self.queryset.filter(guiarecepcion=recepcionmp_pk)
        serializer = DetalleRecepcionMpSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class EnvasesMpViewSet(viewsets.ModelViewSet):

    queryset = EnvasesMp.objects.all()
    serializer_class = EnvasesMpSerializer
    permission_classes = [IsAuthenticated, ]
