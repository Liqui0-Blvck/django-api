from django.shortcuts import render
from rest_framework import viewsets
from inventario_snab.models import *
from inventario_snab.serializer import *
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer
    
class ProductoEnContenedorViewSet(viewsets.ModelViewSet):
    queryset = ProductoEnContenedor.objects.all()
    serializer_class = ProductoEnContenedorSerializer
    
class OrdenDeCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenDeCompra.objects.all()
    serializer_class = OrdenDeCompraSerializer
    