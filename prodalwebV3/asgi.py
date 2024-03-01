import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
# from clientemqtt.consumers import BalanzaMQTT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prodalwebV3.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
})