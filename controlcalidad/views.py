from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User

class CCRecepcionMateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = CCRecepcionMateriaPrima.objects.all()
    #serializer_class = CCRecepcionMateriaPrimaSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CCRecepcionMateriaPrimaSerializer
        return DetalleCCRecepcionMateriaPrimaSerializer
    
    def retrieve(self, request, pk=None):
        ccrecepcionmp = CCRecepcionMateriaPrima.objects.get(pk=pk)
        serializer = self.get_serializer(ccrecepcionmp)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        user = request.user
        request_data = {'cc_registrado_por': user.id, **request.data}
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['get'])
    def total_guias_cc_recepcion_aprobadas(self, request):
        total_guias_cc_aprobadas = CCRecepcionMateriaPrima.objects.filter(estado_cc="1").count()
        return Response(total_guias_cc_aprobadas)
    
    @action(detail=False, methods=['get'])
    def total_guias_cc_recepcion_pendientes(self, request):
        total_guias_cc_pendientes = CCRecepcionMateriaPrima.objects.filter(estado_cc="2").count()
        return Response(total_guias_cc_pendientes)
