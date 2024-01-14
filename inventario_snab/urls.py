from django.urls import path
from rest_framework import routers
from inventario_snab.views import *


router = routers.DefaultRouter()
router.register(r'producto', ProductoViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'proveedor', ProveedorViewSet)
router.register(r'contenedor', ContenedorViewSet)
router.register(r'producto-contenedor', ProductoEnContenedorViewSet)
router.register(r'orden-compra', OrdenDeCompraViewSet)
urlpatterns = router.urls
