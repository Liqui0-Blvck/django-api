from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import action
from django.contrib.contenttypes.models import *


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
        # queryset = get_object_or_404(self.get_queryset(),produccion=produccion, pk=pk)
        queryset = LotesPrograma.objects.get(pk = pk, produccion = produccion)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
    
    def list(self, request, produccion_pk=None):
        produccion = get_object_or_404(Produccion, pk=produccion_pk)
        queryset = LotesPrograma.objects.filter(produccion=produccion)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'], url_path='registrar_lotes/(?P<pks_lotes>[^/.]+)')
    def registrar_lotes(self, request, pks_lotes=None, produccion_pk=None):
        pks_list = pks_lotes.split(',')
    
        for x in pks_list:
            envase = get_object_or_404(EnvasesPatioTechadoExt, pk = x)
            produccion = get_object_or_404(Produccion, pk = produccion_pk)
            LotesPrograma.objects.update_or_create(produccion = produccion, bodega_techado_ext = envase)
            # try:
            # except:
            #     pks_invalidos = []
            #     pks_invalidos.append(x)
            #     return Response({ 'message': 'Fue mal', 'pks_invalidos': pks_invalidos},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({ 'message': 'Creado con exito'}, status=status.HTTP_201_CREATED)
        

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
        # ct_g1 = ContentType.objects.get_for_model(BodegaG1)
        # ct_g2 = ContentType.objects.get_for_model(BodegaG2)
        # ct_g1r = ContentType.objects.get_for_model(BodegaG1Reproceso)
        # ct_g2r = ContentType.objects.get_for_model(BodegaG2Reproceso)
        
        # # data = {
        # #     "reproceso": reproceso.pk,
        # #     "tipo_bin_bodega":
        # # }
        produccion = get_object_or_404(self.get_queryset(),reproceso=reproceso, pk=pk)
        serializer = self.get_serializer(produccion)
        return Response(serializer.data)
    
    def list(self, request, reproceso_pk=None, ):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        queryset = get_list_or_404(BinsEnReproceso, reproceso=reproceso)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request, *args, **kwargs):
        reproceso = get_object_or_404(Reproceso, pk=self.kwargs['reproceso_pk'])
        nombre_model = request.data.get('tipo_bin_bodega', None)
        if nombre_model:
            try:
                ct = ContentType.objects.get(model=nombre_model)
                request.data['tipo_bin_bodega'] = ct.pk
                request.data['reproceso'] = reproceso.pk
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ContentType.DoesNotExist:
                return Response({"error": "El modelo especificado no existe."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "El nombre del modelo no está presente en los datos del request."}, status=status.HTTP_400_BAD_REQUEST)
    

    
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





