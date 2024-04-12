from django.urls import path, include
from .views import *
from rest_framework_nested import routers
app_name = 'bodegas'

router = routers.SimpleRouter()
router.register(r'patio-exterior', PatioTechadoExteriorViewset)
router.register(r'bin-bodega', BinBodegaViewSet)
envases_guia = routers.NestedSimpleRouter(router, r'patio-exterior', lookup='guia_patio__id_recepcion')
envases_guia.register(r'envase-guia-patio', EnvasesPatioTechadoExteriorViewset)


router.register(r'bodega-g1', BodegaG1ViewSet)
router.register(r'bodega-g2', BodegaG2ViewSet)

router.register(r'bodega-g1-reproceso', BodegaG1ReprocesoViewSet)
router.register(r'bodega-g2-reproceso', BodegaG2ReprocesoViewSet)

router.register(r'bodega-residuos', BodegaResiduosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(envases_guia.urls)),
]
