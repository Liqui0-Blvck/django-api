from django.urls import path, include
from rest_framework_nested import routers
from .views import *

app_name = 'core'

router = routers.SimpleRouter()
router.register(r'perfil', PerfilViewSet)
router.register(r'colosos', ColosoViewSet)
router.register(r'operarios', OperarioViewSet)
router.register(r'tractores', TractorViewSet)
router.register(r'etiquetas-zpl', EtiquetasZplViewSet)
router.register(r'choferes', ChoferViewSet)
router.register(r'camiones', CamionViewSet)
router.register(r'cargo-perfil', CargoPerfilViewSet)
router.register(r'personalizacion-perfil', PersonalizacionPerfilViewSet)


tractor_coloso = routers.NestedSimpleRouter(router, r'tractores', lookup='tractores')
tractor_coloso.register(r'coloso-tractor', TractorColosoViewSet)

urlpatterns = [
    path(r'registros/', include(router.urls)),
    path(r'registros/', include(tractor_coloso.urls)),
    path('users/<int:id>', UserAPIView.as_view()),
    path('registro-usuario/', UserRegisterCreateAPIView.as_view()),
]