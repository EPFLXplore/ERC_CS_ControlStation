import json
from channels.generic.websocket import AsyncWebsocketConsumer

import MVC_node.models.utils as utils


"""

Data format :
{

    'active': bool,
    'minutes': int,
    'seconds': int,

}

"""


class TimerConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_group_name = 'tab_timer'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send(text_data=json.dumps(
            {
                "active":utils.timer.is_running,
                "duration":utils.timer.duration,
                }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, data):

        #update timer model
        utils.timer.is_running = data['active']
        utils.timer.duration = 60 * data['minutes'] + data['seconds']

        m,s = utils.timer.get_time()
        

        # Update every frontend
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'broadcast_timer',
                'active': data['active'],
                'minutes': m,
                'seconds': s,
            }
        )

    # Receive message from room group
    async def broadcast_timer(self, data_json):

        m,s = utils.timer.get_time()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'active': data_json['active'],
                'minutes': m,
                'seconds': s,
        }))
