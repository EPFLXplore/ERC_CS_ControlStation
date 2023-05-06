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
        
        self.tab_group_name = 'tab_info_elec'

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
                'type': 'broadcast_info_elec',
                'humidity': data_json['humidity'],
                'temperature': data_json['temperature'],
                'conductivity': data_json['conductivity'],
                'mass_1': data_json['mass_1'],
                'mass_2': data_json['mass_2'],
                'concentration': data_json['concentration'],
                'pH': data_json['pH'],
            }
        )

    # Receive message from room group
    async def broadcast_info_elec(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'type': 'broadcast_info_elec',
                'humidity': data_json['humidity'],
                'temperature': data_json['temperature'],
                'conductivity': data_json['conductivity'],
                'mass_1': data_json['mass_1'],
                'mass_2': data_json['mass_2'],
                'concentration': data_json['concentration'],
                'pH': data_json['pH'],
        }))
