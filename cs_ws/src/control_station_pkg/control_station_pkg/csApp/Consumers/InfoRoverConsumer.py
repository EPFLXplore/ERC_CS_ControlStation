import json

from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :
{
    'state' : string,


"""


class InfoRoverConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # self.tab_name = self.scope['url_route']['kwargs']['tab_name']
        self.tab_name = 'homepage'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave tab group
        await self.channel_layer.group_discard(
            self.tab_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'message': message,
                
            }
        )

    # Receive message from tab group
    async def topic_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))