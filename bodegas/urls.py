from django.urls import path, include
from .views import *
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'cc-guiainterna', CCGuiaInternaViewset)
router.register(r'patio-techado-ex', PatioTechadoExteriorViewset)
router.register(r'patio-techado-ex-id', PatioTechadoExteriorUpdatedViewset)
router.register(r'envase-patio-techado-ex', EnvasesPatioTechadoExteriorViewset)


urlpatterns = [
    path('', include(router.urls))
]
