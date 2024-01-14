from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100, blank=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null = True)
    rut = models.CharField(max_length=100, blank=True, null = True)
    correo = models.EmailField(max_length=255, blank=True, null = True)
    contacto = models.CharField(max_length=100, blank=True, null = True)
    direccion = models.CharField(max_length=100, blank=True, null = True)

    def __str__(self):
        return self.nombre
    
    
class Contenedor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=100, blank=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    capacidad_maxima = models.PositiveIntegerField(blank=True, null=True)
    observaciones = models.TextField()
    productos = models.ManyToManyField(Producto, through='ProductoEnContenedor')
    
    def __str__(self):
        return self.nombre
    
class ProductoEnContenedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    contenedor = models.ForeignKey(Contenedor, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Producto en Categoria'

    
class ProductoProveedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Producto en Categoria'
    

class OrdenDeCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    numero_orden = models.PositiveBigIntegerField(default=0)
    # productos = models.ManyToManyField('ProductoProveedor')
    
    def crear_producto(self, nombre, descripcion, fabricante, cantidad, categoria):
        producto = Producto.objects.create(
            nombre = nombre,
            descripcion = descripcion,
            fabricante = fabricante,
            cantidad = cantidad,
            categoria = categoria
        )
        
        ProductoProveedor.objects.create(producto=producto, proveedor=self.proveedor)
        return producto
    
    def __str__(self):
        return 'Producto en Categoria'
    
    
    

    
    