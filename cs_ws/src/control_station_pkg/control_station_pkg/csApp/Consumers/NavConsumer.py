import json
from re import X
from zlib import Z_NO_COMPRESSION
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


"""

Data format :
{
    'position' : [float] * 3
    'orientation' : [float] * 3
    'linVel' : [float] * 3
    'angVel' : [float] * 3
    'steering_wheel_ang': [float] * 4
    'steering_wheel_state': [float] * 4
    'driving_wheel_ang': [float] * 4
    'driving_wheel_state': [float] * 4
    'path' : [[float, float]]       array of 2 points
    '' : string
    '' : string
}

"""




class NavConsumer(WebsocketConsumer):
    
    def connect(self):

        self.tab_group_name = 'nav'

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
                'type': 'nav_message',
                'position'   : data_json['position'],
                'orientation': data_json['orientation'],
                # 'linVel'     : data_json['linVel'],
                # 'angVel'     : data_json['angVel'],
                'current_goal' : data_json['current_goal'],
                'wheel_ang' : data_json['wheel_ang'],
                'path' : data_json['path'],
            }
        )

    # Receive message from room group
    def nav_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'position'   : event['position'],
                'orientation': event['orientation'],
                # 'linVel'     : event['linVel'],
                # 'angVel'     : event['angVel'],
                'current_goal' : event['current_goal'],
                'wheel_ang' : event['wheel_ang'],
                'path' : event['path'],
        }))
