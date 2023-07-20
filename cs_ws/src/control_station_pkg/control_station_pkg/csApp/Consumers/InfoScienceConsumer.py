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
        
        self.tab_group_name = 'tab_info_science'

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
                'type': 'broadcast_info_science',
                'state': data_json['state'],
                'motor_pos': data_json['motor_pos'],
                'motor_speed': data_json['motor_speed'],
                'motor_current': data_json['motor_current'],
                'drill_speed': data_json['drill_speed'],
                'limt_switch_1': data_json['limt_switch_1'],
                'limt_switch_2': data_json['limt_switch_2'],
                'limt_switch_3': data_json['limt_switch_3'],
                'limt_switch_4': data_json['limt_switch_4'],
            }
        )

    # Receive message from room group
    async def broadcast_info_science(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'state': data_json['state'],
                'motor_pos': data_json['motor_pos'],
                'motor_speed': data_json['motor_speed'],
                'motor_current': data_json['motor_current'],
                'drill_speed': data_json['drill_speed'],
                'limt_switch_1': data_json['limt_switch_1'],
                'limt_switch_2': data_json['limt_switch_2'],
                'limt_switch_3': data_json['limt_switch_3'],
                'limt_switch_4': data_json['limt_switch_4'],
        }))
