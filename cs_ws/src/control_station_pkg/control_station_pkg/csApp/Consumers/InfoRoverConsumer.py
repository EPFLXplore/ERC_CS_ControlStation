import json

from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :
{
    'state' : string,


"""


class InfoRoverConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):

        self.tab_group_name = 'tab_info_rover'

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
    
    async def receive(self, data):
        data_json = json.loads(data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'broadcast_info_rover',
                'state': data_json['state'],
                
            }
        )

    # Receive message from tab group
    async def broadcast_info_rover(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'state': data_json['state'],
        }))