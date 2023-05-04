import json
from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :

{

    "state" : state,
    'motor_pos' : float,
    'motor_speed' : float,
    'motor_current' : float,
    'drill_speed' : float,
    'limt_switch_1' : bool,
    'limt_switch_2' : bool,

}

"""


class InfoScienceConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.tab_name = 'science'
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
        parameters     = text_data_json['params']
        particle_sizes = text_data_json['particle_sizes']
        volumes        = text_data_json['volumes']
        densities      = text_data_json['densities']
        colors         = text_data_json['colors']
        humidity       = text_data_json['humidity']
        infos          = text_data_json['infos']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'params'        : parameters,
                'particle_sizes': particle_sizes,
                'volumes'       : volumes,
                'densities'     : densities,
                'colors'        : colors,
                'humidity'      : humidity,
                'infos'         : infos
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        params         = event['params']
        particle_sizes = event['particle_sizes']
        volumes        = event['volumes']
        densities      = event['densities']
        colors         = event['colors']
        humidity       = event['humidity']
        infos          = event['infos']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'params'        : params,
            'particle_sizes': particle_sizes,
            'volumes'       : volumes,
            'densities'     : densities,
            'colors'        : colors,
            'humidity'      : humidity,
            'infos'         : infos
        }))
