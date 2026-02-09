from django.urls import path
from .consumers import PersonlChatConsumer

websocket_urlpatterns = [
    path('ws/chat/', PersonlChatConsumer.as_asgi())
]