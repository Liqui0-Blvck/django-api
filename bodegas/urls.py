from django.urls import path, include
from .views import *
from rest_framework_nested import routers
app_name = 'bodegas'

router = routers.SimpleRouter()
router.register(r'patio-exterior', PatioTechadoExteriorViewset)
router.register(r'bin-bodega', BinBodegaViewSet)
envases_guia = routers.NestedSimpleRouter(router, r'patio-exterior', lookup='guia_patio')
envases_guia.register(r'envase-guia-patio', EnvasesPatioTechadoExteriorViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(envases_guia.urls)),
]
