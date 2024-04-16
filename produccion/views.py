from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import action
from django.contrib.contenttypes.models import *
from django.http import Http404


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
        print(pks_list)
        produccion = get_object_or_404(Produccion, pk = produccion_pk)
        for x in pks_list:
            envase = EnvasesPatioTechadoExt.objects.get(pk = x)
            LotesPrograma.objects.update_or_create(produccion = produccion, bodega_techado_ext = envase)
        return Response({ 'message': 'Creado con exito'}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['DELETE'], url_path='eliminar_lotes/(?P<pks_lotes>[^/.]+)')  
    def eliminar_lotes(self, request, pks_lotes=None, produccion_pk=None):
        pks_list = pks_lotes.split(',')
        produccion = get_object_or_404(Produccion,pk = produccion_pk)
        LotesPrograma.objects.filter(produccion = produccion, bodega_techado_ext__in = list(pks_list)).delete()
        return Response({ 'message': 'Lote Eliminado con exito'})
    
    @action(detail=False, methods=['PUT', 'PATCH'], url_path='actualizar_estados_lotes/(?P<pks_lotes>[^/.]+)')
    def actualizar_estados_lotes(self, request, pks_lotes=None, produccion_pk=None):
        pks_list = pks_lotes.split(',')
        produccion = get_object_or_404(Produccion,pk = produccion_pk)
        for x in pks_list:
            envase = EnvasesPatioTechadoExt.objects.get(pk = x)
            LotesPrograma.objects.filter(produccion = produccion, bodega_techado_ext = envase).update(bin_procesado = True)
        return Response({ 'message': 'Lote Actualizados con exito'})
    
        
              
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


    def create(self, request, reproceso_pk=None,*args, **kwargs):
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        nombre_model = request.data.get('tipo_bin_bodega', None)
        id_binbodega = request.data.get('id_bin_bodega', None)
        if nombre_model == 'bodegag1':
            ct = ContentType.objects.get_for_model(BodegaG1)
            binbodega = get_object_or_404(BodegaG1, pk=id_binbodega)
        elif nombre_model == 'bodegag2':
            ct = ContentType.objects.get_for_model(BodegaG2)
            binbodega = get_object_or_404(BodegaG2, pk=id_binbodega)
        elif nombre_model == 'bodegag1reproceso':
            ct = ContentType.objects.get_for_model(BodegaG1Reproceso)
            binbodega = get_object_or_404(BodegaG1Reproceso, pk=id_binbodega)
        elif nombre_model == 'bodegag2reproceso':
            ct = ContentType.objects.get_for_model(BodegaG2Reproceso)
            binbodega = get_object_or_404(BodegaG2Reproceso, pk=id_binbodega)
        else:
            return Response({"error":"No hay bin que coincida"}, status=status.HTTP_400_BAD_REQUEST)
        datos = {
            "id_bin_bodega": binbodega.pk,
            "tipo_bin_bodega": ct.pk,
            "reproceso": reproceso.pk
        }
        serializer = self.get_serializer(data=datos)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    @action(detail=False, methods=['POST'], url_path='registrar_bins/(?P<pks_lotes>[^/.]+)')
    def registrar_bins(self, request, pks_lotes=None, reproceso_pk=None):
        pks_list = pks_lotes.split(',')
        reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)
        
        print(pks_list)

        # Lista de modelos en los que verificar la existencia del ID
        modelos = [BodegaG1, BodegaG2, BodegaG1Reproceso, BodegaG2Reproceso]
        
        bin_reproceso = None
        print(bin_reproceso)
        
        # bin_en_reproceso = BodegaG2.objects.get(pk = pks_list[0])
        # print(bin_en_reproceso)
        
        
        for pk in pks_list:
            for modelo in modelos:
                try:
                    bin_reproceso = get_object_or_404(modelo, pk=pk)
                    print("estoy imprimiendome desde el bucle", bin_reproceso)
                    ct = ContentType.objects.get_for_model(bin_reproceso)
                    print(ct)
                    datos = {
                        "id_bin_bodega": bin_reproceso.pk,
                        "tipo_bin_bodega": ct.pk,
                        "reproceso": reproceso.pk
                    }
                    serializer = self.get_serializer(data=datos)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
                    break  # Si se encuentra en algún modelo, salir del bucle
                except Http404:
                    continue  # Si no se encuentra en este modelo, intentar con el siguiente
            
            if bin_reproceso is not None:
                # Se encontró en algún modelo
                break
        else:
            # No se encontró en ninguno de los modelos
            print("# No se encontró en ninguno de los modelos")
        
        return Response({ 'message': 'Ningún objeto encontrado para los IDs proporcionados'})

    
    
    # @action(detail=False, methods=['POST'], url_path='registrar_bins/(?P<pks_lotes>[^/.]+)')
    # def registrar_bins(self, request, pks_lotes=None, reproceso_pk=None):
    #     pks_list = pks_lotes.split(',') # type: ignore
    #     reproceso = get_object_or_404(Reproceso, pk=reproceso_pk)

    #     for x in pks_list:
    #         print(x)
    #   
    # bin_reproceso = None
            
    #         print(bin_reproceso)
    #         try:
    #             bin_reproceso = get_object_or_404(BodegaG1, pk = x)
    #             bin_reproceso = get_object_or_404(BodegaG2, pk = x)
    #             bin_reproceso = get_object_or_404(BodegaG1Reproceso, pk = x)
    #             bin_reproceso = get_object_or_404(BodegaG2, pk = x)
                
                
    #             # bin_en_reproceso = BinsEnReproceso.objects.get(pk = x)
    #             # print(bin_en_reproceso)
    #         except:
    #           print('An exception occurred')
        
    #     print()
        
    # @action(detail=False, methods=['POST'], url_path='registrar_lotes/(?P<pks_lotes>[^/.]+)')
    # def registrar_lotes(self, request, pks_lotes=None, produccion_pk=None):
    #     pks_list = pks_lotes.split(',')
    #     print(pks_list)
    #     produccion = get_object_or_404(Produccion, pk = produccion_pk)
    #     for x in pks_list:
    #         envase = EnvasesPatioTechadoExt.objects.get(pk = x)
    #         LotesPrograma.objects.update_or_create(produccion = produccion, bodega_techado_ext = envase)
    #     return Response({ 'message': 'Creado con exito'}, status=status.HTTP_201_CREATED)
        
       
    
    # @action(detail=False, methods=['POST'], url_path='registrar_bins/(?P<pks_lotes>[^/.]+)')
    # def registrar_bins(self, request, pks_lotes=None, reproceso_pk=None):
    #     pks_list = pks_lotes.split(',')
    #     reproceso = get_object_or_404(Reproceso, pk = reproceso_pk)
    #     print(reproceso)
    #     print(pks_list)
    #     BinsEnReproceso.objects.update_or_create(reproceso = reproceso, id_bin_bodega__in = list(pks_list))
    #     # LotesPrograma.objects.update_or_create(reproceso = reproceso, bodega_techado_ext__in = list(pks_list))
    #     return Response({ 'message': 'Creado con exito'}, status=status.HTTP_201_CREATED)
    
    # @action(detail=False, methods=['DELETE'], url_path='eliminar_lotes/(?P<pks_lotes>[^/.]+)')  
    # def eliminar_lotes(self, request, pks_lotes=None, reproceso_pk=None):
    #     pks_list = pks_lotes.split(',')
    #     reproceso = get_object_or_404(Reproceso,pk = reproceso_pk)
    #     LotesPrograma.objects.filter(reproceso = reproceso, bodega_techado_ext__in = list(pks_list)).delete()
    #     return Response({ 'message': 'Lote Eliminado con exito'})
    
    # @action(detail=False, methods=['PUT', 'PATCH'], url_path='actualizar_estados_lotes/(?P<pks_lotes>[^/.]+)')
    # def actualizar_estados_lotes(self, request, pks_lotes=None, reproceso_pk=None):
    #     pks_list = pks_lotes.split(',')
    #     reproceso = get_object_or_404(Reproceso,pk = reproceso_pk)
    #     LotesPrograma.objects.filter(reproceso = reproceso, bodega_techado_ext__in = list(pks_list)).update(bin_procesado = True)
    #     return Response({ 'message': 'Lote Actualizados con exito'})
    
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




