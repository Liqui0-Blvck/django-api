from http.client import METHOD_NOT_ALLOWED
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import *
from .models import *
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class CCRecepcionMateriaPrimaViewSet(viewsets.ModelViewSet):
    search_fields = ['recepcionmp__id']
    filter_backends = (filters.SearchFilter, )
    queryset = CCRecepcionMateriaPrima.objects.all()    
    #serializer_class = CCRecepcionMateriaPrimaSerializer
    permission_classes = [IsAuthenticated,]
    
    
    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return CCRecepcionMateriaPrimaSerializer
        return DetalleCCRecepcionMateriaPrimaSerializer
    
    def retrieve(self, request, pk=None):
        ccrecepcionmp = get_object_or_404(CCRecepcionMateriaPrima, pk=pk)
        serializer = self.get_serializer(ccrecepcionmp)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        request_data = request.data
        datos_front = request.data
        print(datos_front)
        serializer = self.get_serializer(data=request_data)
        if serializer.is_valid():
            usuario = User.objects.get(pk = datos_front['cc_registrado_por'])
            control_existente = CCRecepcionMateriaPrima.objects.get(recepcionmp = datos_front['recepcionmp'])
            if control_existente:
                control_existente.humedad = datos_front['humedad']
                control_existente.presencia_insectos = datos_front['presencia_insectos']
                control_existente.observaciones = datos_front['observaciones']
                control_existente.cc_registrado_por = usuario
                control_existente.save()
            else:
                print('creo que no deberia llegar aqui')
                self.perform_create(serializer)
            
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['get'])
    def total_guias_cc_recepcion_aprobadas(self, request):
        total_guias_cc_aprobadas = CCRecepcionMateriaPrima.objects.filter(estado_cc="1").count()
        return Response(total_guias_cc_aprobadas)
    
    @action(detail=False, methods=['get'])
    def total_guias_cc_recepcion_pendientes(self, request):
        total_guias_cc_pendientes = CCRecepcionMateriaPrima.objects.filter(estado_cc="2").count()
        return Response(total_guias_cc_pendientes)

    @action(detail=True, methods=['POST'])
    def registra_muestra_lote(self, request, pk=None):
        ccrecep = get_object_or_404(CCRecepcionMateriaPrima, pk=pk)
        serializadorcdr = CCRendimientoSerializer(data=request.data)
        serializadorcdr.is_valid(raise_exception=True)
        serializadorcdr.save(cc_recepcionmp=ccrecep)
        return Response(serializadorcdr.data, status=status.HTTP_201_CREATED)
    

    @action(detail=True, methods=['GET'])
    def lista_muestra_lote(self, request, pk=None):
        ccrecep = get_object_or_404(CCRecepcionMateriaPrima, pk=pk)
        listamuestras = get_list_or_404(CCRendimiento, cc_recepcionmp=ccrecep)
        serializer = CCRendimientoSerializer(listamuestras, many=True)
        return Response(serializer.data)
    

class CCRendimientoViewSet(viewsets.ModelViewSet):
    queryset = CCRendimiento.objects.all()
    serializer_class = CCRendimientoSerializer
    permission_classes = [IsAuthenticated,]
    
    def retrieve(self, request,cc_recepcionmp_pk=None , pk=None):
        ccrecep = get_object_or_404(CCRecepcionMateriaPrima, pk=cc_recepcionmp_pk)
        ccrendimiento = get_object_or_404(CCRendimiento, pk=pk, cc_recepcionmp=ccrecep)
        serializer = self.get_serializer(ccrendimiento)
        return Response(serializer.data)
    
    def list(self, request, cc_recepcionmp_pk=None):
        queryset = self.queryset.filter(cc_recepcionmp=cc_recepcionmp_pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
   

class CCPepaViewSet(viewsets.ModelViewSet):
    queryset = CCPepa.objects.all()
    serializer_class = CCPepaSerializer
    permission_classes = [IsAuthenticated,]
    

    def retrieve(self, request,cc_recepcionmp_pk=None,cc_rendimiento_pk=None, pk=None):
        print(self.kwargs)
        ccrecep = get_object_or_404(CCRecepcionMateriaPrima, pk=cc_recepcionmp_pk)
        ccrendimiento = get_object_or_404(CCRendimiento, pk=cc_rendimiento_pk, cc_recepcionmp=ccrecep)
        ccpepa = get_object_or_404(CCPepa, pk=pk, cc_rendimiento=ccrendimiento)
        serializer = self.get_serializer(ccpepa)
        return Response(serializer.data)        
    
    def list(self, request,cc_recepcionmp_pk=None,cc_rendimiento_pk=None,):
        ccrecep = get_object_or_404(CCRecepcionMateriaPrima, pk=cc_recepcionmp_pk)
        ccrendimiento = get_object_or_404(CCRendimiento, pk=cc_rendimiento_pk, cc_recepcionmp=ccrecep)
        ccpepa = get_object_or_404(CCPepa, cc_rendimiento=ccrendimiento)
        serializer = self.get_serializer(ccpepa)
        return Response(serializer.data)


class FotosCCRecepcionMateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = FotosCC.objects.all()
    serializer_class = FotosCCRecepcionMateriaPrimaSerializer
    permission_classes = [IsAuthenticated,]
    

    
    