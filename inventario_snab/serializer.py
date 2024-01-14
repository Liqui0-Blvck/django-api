from rest_framework import serializers
from inventario_snab.models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.SerializerMethodField()
    categoria_descripcion = serializers.SerializerMethodField()
    
    class Meta:
        model = Producto
        exclude = ['categoria']
        
    def get_categoria_nombre(self, instance):
        return instance.categoria.nombre if instance.categoria else None
    
    def get_categoria_descripcion(self, instance):
        return instance.categoria.descripcion if instance.categoria else None

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ContenedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedor
        fields = '__all__'
        
class ProductoEnContenedorSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.SerializerMethodField()
    caja_contenedora = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductoEnContenedor
        fields = '__all__'
        
    def get_nombre_producto(self, instance):
        return instance.producto.nombre if instance.producto else None
    
    def get_caja_contenedora(self, instance):
        return instance.contenedor.nombre if instance.contenedor else None
    
class OrdenDeCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDeCompra
        fields = '__all__'
        
        