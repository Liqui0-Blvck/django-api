from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status


class GuiaRecepcionMPViewSet(viewsets.ModelViewSet):
    queryset = GuiaRecepcionMP.objects.all()
    serializer_class = GuiaRecepcionMPSerializer
    permission_classes = [IsAuthenticated, ]


class RecepcionMpViewSet(viewsets.ModelViewSet):
    queryset = RecepcionMp.objects.all()
    serializer_class = RecepcionMpSerializer
    permission_classes = [IsAuthenticated, ]
    
    
    def retrieve(self, request, recepcionmp_pk=None, pk=None):
        queryset = self.queryset.filter(guiarecepcion=recepcionmp_pk, pk=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, recepcionmp_pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        guiarecepcion = GuiaRecepcionMP.objects.get(pk=recepcionmp_pk)
        serializer.save(guiarecepcion=guiarecepcion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, recepcionmp_pk=None):
        queryset = self.queryset.filter(guiarecepcion=recepcionmp_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)