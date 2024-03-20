from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import *
import json


class GuiaRecepcionMPViewSet(viewsets.ModelViewSet):
    queryset = GuiaRecepcionMP.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    
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
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return RecepcionMpSerializer
        return DetalleRecepcionMpSerializer
    
    def retrieve(self, request, recepcionmp_pk=None, pk=None):
        guiarecepcion = GuiaRecepcionMP.objects.get(pk=recepcionmp_pk)
        queryset = RecepcionMp.objects.get(guiarecepcion=guiarecepcion, pk=pk)
        serializer = RecepcionListMpSerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        envases = request.data.get('envases', [])
        serializador_envases = EnvasesGuiaRecepcionMpSerializer(data=envases, many=True)
        serializador_envases.is_valid(raise_exception=True)
        serializador_envases.save(recepcionmp=serializer.save())
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, recepcionmp_pk=None):
        queryset = self.queryset.filter(guiarecepcion=recepcionmp_pk)
        serializer = DetalleRecepcionMpSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class EnvasesMpViewSet(viewsets.ModelViewSet):

    queryset = EnvasesMp.objects.all()
    serializer_class = EnvasesMpSerializer

class EnvasesGuiaMPViewSet(viewsets.ModelViewSet):
    queryset = EnvasesGuiaRecepcionMp.objects.all()
    
    def get_serializer_class(self): 
        return EnvasesGuiaRecepcionSerializer   
    
    def create(self, request, *args, **kwargs):
        envase_guia = request.data.get('envases', '[]')
        envases = json.loads(envase_guia)
        envase_ids_in_request = [envase.get('envase') for envase in envases]
        envase_instance = EnvasesGuiaRecepcionMp.objects.filter(envase__in=envase_ids_in_request)
        envase_instance_list = set(envase_instance.values_list( 'id', flat=True))
        
        
        for envase in envases:
            recepcionmp = RecepcionMp.objects.get(pk=envase['recepcionmp'])
            envases_en_recepcionmp = recepcionmp.envasesguiarecepcionmp_set.filter(recepcionmp=envase['recepcionmp'])
            envases_en_recepcionmp_list = set(envases_en_recepcionmp.values_list('id', flat=True))
            eliminables =  set(envases_en_recepcionmp_list) - set(envase_instance_list)
            recepcionmp.envasesguiarecepcionmp_set.filter(pk__in=eliminables).delete()
            envase_existente = EnvasesGuiaRecepcionMp.objects.filter(recepcionmp=envase['recepcionmp'], envase=envase['envase']).first()
            if envase_existente:
                pass
            else:
                serializer = self.get_serializer(data=envase)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response("Envases creados o actualizados correctamente", status=status.HTTP_201_CREATED)
    
    

class EstadoRecepcionUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = RecepcionMp.objects.all()
    serializer_class = EstadoRecepcionUpdateSerializer
    
    
    
class EstadoGuiaRecepcionUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = GuiaRecepcionMP.objects.all()
    serializer_class = EstadoGuiaRecepcionUpdateSerializer
    
    
class LoteRechazadoViewset(viewsets.ModelViewSet):
    queryset = LoteRecepcionMpRechazadoPorCC.objects.all()
    serializer_class = LoteRechazadoSerializer  