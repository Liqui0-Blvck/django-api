from django.urls import path, include
from rest_framework_nested import routers
from .views import *

app_name = 'controlcalidad'

router = routers.SimpleRouter()
router.register(r'control-calidad/recepcionmp', CCRecepcionMateriaPrimaViewSet)
#router.register(r'envasesmp', EnvasesMpViewSet)

# lotes_guia = routers.NestedSimpleRouter(router, r'recepcionmp', lookup='recepcionmp')
# lotes_guia.register(r'lotes', RecepcionMpViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    # path(r'', include(lotes_guia.urls)),
]