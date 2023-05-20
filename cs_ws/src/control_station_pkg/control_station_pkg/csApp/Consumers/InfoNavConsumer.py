import json
from re import X
from zlib import Z_NO_COMPRESSION
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync


"""

Data format :
{
    'position' : [float] * 3
    'orientation' : [float] * 3
    'linVel' : [float] * 3
    'angVel' : [float] * 3
    'current_goal' : [float] * 3
    'wheel_ang': [float] * 4
}

"""




class InfoNavConsumer(WebsocketConsumer):
    
    def connect(self):

        self.tab_group_name = 'info_nav'

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

        print("received in nav")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.tab_group_name,
            {
                'type': 'nav_message',
                'position'   : data_json['position'],
                'orientation': data_json['orientation'],
                'linVel'     : data_json['linVel'],
                'angVel'     : data_json['angVel'],
                'current_goal' : data_json['current_goal'],
                'wheel_ang' : data_json['wheel_ang'],
            }
        )




    # Receive message from room group
    def nav_message(self, event):

        print("broadcast_info_nav")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
                'position'   : event['position'],
                'orientation': event['orientation'],
                'linVel'     : event['linVel'],
                'angVel'     : event['angVel'],
                'current_goal' : event['current_goal'],
                'wheel_ang' : event['wheel_ang'],
        }))
