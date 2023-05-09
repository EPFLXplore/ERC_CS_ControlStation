import json
from channels.generic.websocket import AsyncWebsocketConsumer

"""

Data format :
{
    'hours' : hours,
    'minutes' : minutes,
    'seconds' : seconds,
    'type' : type
    'message' : message
}

"""


class LogConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.tab_group_name = 'tab_log'

        print("channels name : " + self.channel_name)

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()



    # Receive message from WebSocket
    async def receive(self, data):

        data_json = json.loads(data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'broadcast_log',
                'hours': data_json['hours'],
                'minutes': data_json['minutes'],
                'seconds': data_json['seconds'],
                'type': data_json['type'],
                'message': data_json['message'],

            }
        )

    # Receive message from room group
    async def broadcast_log(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'type': 'broadcast_log',
                'hours': data_json['hours'],
                'minutes': data_json['minutes'],
                'seconds': data_json['seconds'],
                'type': data_json['type'],
                'message': data_json['message'],

        }))
