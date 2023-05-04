import json
from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :
{
    'humidity' : float,
    'temperature' : float,
    'conductivity' : float,
    'mass_1' : float,
    'mass_2' : float,
    'concentration' : float,
    'pH' : float,
    

    accelerometer
    Spectro [] * 17

}

"""


class InfoElecConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.tab_name = 'logs'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()



    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        exceptions = text_data_json['exceptions']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'exceptions': exceptions
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        exceptions = event['exceptions']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'exceptions': exceptions
        }))
