from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    lookup_field = 'user'
    # permission_classes = [IsAuthenticated]
    
class ColosoViewSet(viewsets.ModelViewSet):

    queryset = Coloso.objects.all()
    serializer_class = ColosoSerializer
    permission_classes = [IsAuthenticated]
    
class OperarioViewSet(viewsets.ModelViewSet):

    queryset = Operario.objects.all()
    serializer_class = OperarioSerializer
    permission_classes = [IsAuthenticated]
    
    
class TractorViewSet(viewsets.ModelViewSet):

    queryset = Tractor.objects.all()
    serializer_class = TractorSerializer
    permission_classes = [IsAuthenticated]
    
class TractorColosoViewSet(viewsets.ModelViewSet):

    queryset = TractorColoso.objects.all()
    serializer_class = TractorColosoSerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, tractores_pk=None, pk=None):
        queryset = self.queryset.filter(tractor=tractores_pk, pk=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, tractores_pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tractor = Tractor.objects.get(pk=tractores_pk)
        serializer.save(tractor=tractor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, tractores_pk=None):
        queryset = self.queryset.filter(tractor=tractores_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class EtiquetasZplViewSet(viewsets.ModelViewSet):

    queryset = EtiquetasZpl.objects.all()
    serializer_class = EtiquetasZplSerializer
    permission_classes = [IsAuthenticated]
    
class ChoferViewSet(viewsets.ModelViewSet):

    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer
    permission_classes = [IsAuthenticated]
    
class CamionViewSet(viewsets.ModelViewSet):

    queryset = Camion.objects.all()
    serializer_class = CamionSerializer
    # permission_classes = [IsAuthenticated]

class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    http_method_names = ['get']
    serializer_class = UserSerializer



class CargoPerfilViewSet(viewsets.ModelViewSet):
    queryset = CargoPerfil.objects.all()
    serializer_class = CargoPerfilSerializer