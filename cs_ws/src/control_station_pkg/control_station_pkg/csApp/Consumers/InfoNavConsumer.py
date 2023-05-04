import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


"""
Data format :
{
    'state' : state,
    'pos_x' : x_pos,
    'pos_y' : y_pos,
    'pos_z' : z_pos,
    'ang_x' : angle,
    'ang_y' : angle,
    'ang_z' : angle,
    'linVel' : linearVelocity,
    'angVel' : angularVelocity,
    'ang_front_left_wheel' : ,
    'ang_front_right_wheel' : ,
    'ang_rear_left_wheel' : ,
    'ang_rear_right_wheel' : ,
    'current_goal' : ,
    'goals' : ,

    '
}

"""


class NavManualConsumer(RoverConsumer):
    
    async def connect(self):
        
        self.tab_group_name = 'nav_manual'

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json  = json.loads(text_data)
        x_pos           = text_data_json['x']
        y_pos           = text_data_json['y']
        linearVelocity  = text_data_json['linVel']
        angularVelocity = text_data_json['angVel']
        joint_position  = text_data_json['joint_pos']
        joint_velocity  = text_data_json['joint_vel']
        hd_mode         = text_data_json['hd_mode']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type'     : 'nav_manual_broadcast',
                'x'        : x_pos,
                'y'        : y_pos,
                'linVel'   : linearVelocity,
                'angVel'   : angularVelocity,
                'joint_pos': joint_position,
                'joint_vel': joint_velocity,
                'hd_mode'  : hd_mode
            }
        )

    # Receive message from room group
    async def nav_manual_broadcast(self, event):
        print(event)

        x_pos           = event['x']
        y_pos           = event['y']
        linearVelocity  = event['linVel']
        angularVelocity = event['angVel']
        joint_position  = event['joint_pos']
        joint_velocity  = event['joint_vel']
        hd_mode         = event['hd_mode']

        print("print : " + event['text'])   

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'x'        : x_pos,
            'y'        : y_pos,
            'linVel'   : linearVelocity,
            'angVel'   : angularVelocity,
            'joint_pos': joint_position,
            'joint_vel': joint_velocity,
            'hd_mode'  : hd_mode
        }))
