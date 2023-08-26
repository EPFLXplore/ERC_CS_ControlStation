import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

"""

Data format :

{

    "state" : int,
    'motors_pos' : float * 2,
    'motors_speed' : float * 3,
    'motors_currents' : float * 3 (?),
    'limit_switches' : int * 4 

}

"""


class ScienceDrillConsumer(WebsocketConsumer):
    
    def connect(self):

        self.tab_group_name = 'science_drill'

        # Join tab group
        async_to_sync(self.channel_layer.group_add)(
            self.tab_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave tab group
        async_to_sync(self.channel_layer.group_discard)(
            self.tab_group_name,
            self.channel_name
        )


    # Receive message from WebSocket
    def receive(self, text_data):

        data_json = json.loads(text_data)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'science_drill_message',
                'state': data_json['state'],
                'motors_pos': data_json['motors_pos'],
                'motors_speed': data_json['motors_speed'],
                'motors_currents': data_json['motors_currents'],
                'limit_switches': data_json['limit_switches'],
            }
        )

    # Receive message from room group
    def science_drill_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'state': event['state'],
                'motors_pos': event['motors_pos'],
                'motors_speed': event['motors_speed'],
                'motors_currents': event['motors_currents'],
                'limit_switches': event['limit_switches'],
        }))
