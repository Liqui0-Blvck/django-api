from django.urls import path, include
from rest_framework_nested import routers
from .views import *

app_name = 'recepcionmp'

router = routers.SimpleRouter()
router.register(r'recepcionmp', GuiaRecepcionMPViewSet)
router.register(r'envasesmp', EnvasesMpViewSet)
router.register(r'envaseguiamp', EnvasesGuiaMPViewSet)
router.register(r'lotes-rechazados', LoteRechazadoViewset)

lotes_guia = routers.NestedSimpleRouter(router, r'recepcionmp', lookup='recepcionmp')
lotes_guia.register(r'lotes', RecepcionMpViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(lotes_guia.urls)),
    path('estado-update/<int:id>', EstadoRecepcionUpdateAPIView.as_view()),
    path('estado-guia-update/<int:id>', EstadoGuiaRecepcionUpdateAPIView.as_view())
]