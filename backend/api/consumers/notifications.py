from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "-"
        if self.scope["user"].is_anonymous:
            # Reject the connection
            await self.close()
        else:
            self.user = self.scope['user']
            self.group_name = self.user.id

            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        group_name = str(self.user.id)

        # Send message to room group
        await self.channel_layer.group_send(
            group_name,
            {
                'type': 'notification',
                'message': message
            }
        )

    # Receive message from room group
    async def notification(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
