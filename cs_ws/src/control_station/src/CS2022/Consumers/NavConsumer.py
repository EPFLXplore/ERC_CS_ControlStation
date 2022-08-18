import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


class NavConsumer(RoverConsumer):
    
    # async def connect(self):
    #     self.room_name = self.scope['url_route']['kwargs']['tab_name']
    #     self.room_group_name = 'chat_%s' % self.room_name

    #     # Join room group
    #     await self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    #     await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_1 = text_data_json['Debug']
        message_2 = text_data_json['Debug2']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'Debug': message_1,
                'Debug2': message_2
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        message_1 = event['Debug']
        message_2 = event['Debug2']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'Debug': message_1,
            'Debug2':message_2
        }))
