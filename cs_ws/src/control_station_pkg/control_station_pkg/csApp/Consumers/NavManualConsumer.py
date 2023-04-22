import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer


class NavManualConsumer(RoverConsumer):
    
    async def connect(self):
        
        self.tab_name = 'manual'
        self.tab_group_name = 'tab_%s' % self.tab_name

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
                'type'     : 'topic_message',
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
    async def topic_message(self, event):
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
