from channels.generic.websocket import AsyncWebsocketConsumer
import json
import secrets


class PersonlChatConsumer(AsyncWebsocketConsumer):
    # TODO: add user-specific token identity
    async def connect(self):
        """Connecting users with websockets into game rooms"""
        room_name = self.scope['url_route']['kwargs'].get('room_name')
        self.room_group_name = room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()


    # TODO: refactor code by splitting the main if block into separate functions
    async def receive(self, text_data):
        """Handling reciving websocket signals"""
        try:
            data = json.loads(text_data)
            socket_type = data["type"]
            user = data["username"]
            if socket_type == "message":
                message = data["message"]
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'user': user
                    }
                )
            elif socket_type == "draw":
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'draw',
                        'username': user,
                        'last_x': data["last_x"],
                        'last_y': data["last_y"],
                        'offset_x': data["offset_x"],
                        'offset_y': data["offset_y"],
			'color': data['color']
                    }
                )
        # FIXME: add proper error handling.
        # FIXME: refactor error handlers
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON format'
            }))


    async def chat_message(self, event):
        """Handling sending chat messages"""
        try:
            message = event["message"]
            user = event["user"]
            await self.send(text_data = json.dumps({"type": "message", "message": message, "user": user}))
        # FIXME: add proper error handling
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': "Error"
            }))


    async def draw(self, event):
        """Handling sending drawing signals to all users in game room"""
        try:
            await self.send(text_data = json.dumps({'type': 'draw', 'color': event['color'], 'username': event["username"], 'last_x': event["last_x"], 'last_y': event['last_y'], 'offset_x': event['offset_x'], 'offset_y': event['offset_y']}))
        # FIXME: add proper error handling
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'error'
            }))
