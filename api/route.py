from django.urls import path
from .consumers import PersonlChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>', PersonlChatConsumer.as_asgi())
]