from channels.generic.websocket import AsyncWebsocketConsumer

class PersonlChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()