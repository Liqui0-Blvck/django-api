from django.urls import path, include
from rest_framework_nested import routers
from .views import *

app_name = 'controlcalidad'

router = routers.SimpleRouter()
router.register(r'control-calidad/recepcionmp', CCRecepcionMateriaPrimaViewSet)
router.register(r'fotos-cc', FotosCCRecepcionMateriaPrimaViewSet)

muestras = routers.NestedSimpleRouter(router, r'control-calidad/recepcionmp', lookup='cc_recepcionmp')
muestras.register(r'muestras', CCRendimientoViewSet)
cdcpepa_muestra = routers.NestedSimpleRouter(muestras, r'muestras', lookup='cc_rendimiento')
cdcpepa_muestra.register(r'cdcpepa', CCPepaViewSet)

router.register(r'produccion/cdc-tarjaresultante', CCTarjaResultanteViewSet)
router.register(r'reproceso/cdc-tarjaresultante', CCTarjaResultanteReprocesoViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(muestras.urls)),
    path(r'', include(cdcpepa_muestra.urls)),
    path('estado-aprobacion-jefatura/<int:id>/', EstadoAprobacionJefaturaAPIView.as_view()),
    path('estado-contramuestra/<int:id>/', EstadoContraMuestraAPIView.as_view())
]