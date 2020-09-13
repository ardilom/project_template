from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import NotificationConsumer
from .token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('socket/<str:token>', NotificationConsumer),
        ]),
    ),
})
