import json
from re import X
from zlib import Z_NO_COMPRESSION
from channels.generic.websocket import AsyncWebsocketConsumer


"""

Data format :
{
    'state' : state,
    'x' : x_pos,
    'y' : y_pos,
    'z' : z_pos,
    'ang_x' : x_angle,
    'ang_y' : y_angle,
    'ang_z' : z_angle,
    'linVel' : linearVelocity,
    'angVel' : angularVelocity,
    'current_goal' : current_goal,
    'goals' : goals,
    'ang_front_right_wheel' : ang_front_right_wheel,
    'ang_front_left_wheel' : ang_front_left_wheel,
    'ang_back_right_wheel' : ang_back_right_wheel,
    'ang_back_left_wheel' : ang_back_left_wheel,
}

"""


class InfoNavConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):

        self.tab_group_name = 'tab_info_nav'

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
                'type'    : 'broadcast_info_nav',
                'state'   : data_json['state'],
                'x'       : data_json['x'],
                'y'       : data_json['y'],
                'z'       : data_json['z'],
                'ang_x'   : data_json['ang_x'],
                'ang_y'   : data_json['ang_y'],
                'ang_z'   : data_json['ang_z'],
                'linVel'  : data_json['linVel'],
                'angVel'  : data_json['angVel'],
                'current_goal' : data_json['current_goal'],
                'goals'   : data_json['goals'],
                'ang_front_right_wheel' : data_json['ang_front_right_wheel'],
                'ang_front_left_wheel'  : data_json['ang_front_left_wheel'],
                'ang_back_right_wheel'  : data_json['ang_back_right_wheel'],
                'ang_back_left_wheel'   : data_json['ang_back_left_wheel'],
            }
        )

    # Receive message from room group
    async def broadcast_info_nav(self, data_json):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'state'   : data_json['state'],
                'x'       : data_json['x'],
                'y'       : data_json['y'],
                'z'       : data_json['z'],
                'ang_x'   : data_json['ang_x'],
                'ang_y'   : data_json['ang_y'],
                'ang_z'   : data_json['ang_z'],
                'linVel'  : data_json['linVel'],
                'angVel'  : data_json['angVel'],
                'current_goal' : data_json['current_goal'],
                'goals'   : data_json['goals'],
                'ang_front_right_wheel' : data_json['ang_front_right_wheel'],
                'ang_front_left_wheel'  : data_json['ang_front_left_wheel'],
                'ang_back_right_wheel'  : data_json['ang_back_right_wheel'],
                'ang_back_left_wheel'   : data_json['ang_back_left_wheel'],
        }))
