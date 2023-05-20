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

        await self.channel_layer.group_add(
            "timer",
            self.channel_name
        )
        
        await self.accept()
        m,s = utils.timer.get_time()
        # Update every frontend
        await self.channel_layer.group_send(
            "timer",
            {
                'type': 'timer_message',
                'active': utils.timer.is_running,
                'minutes': m,
                'seconds': s,
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            "timer",
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        data = json.loads(text_data)
        #update timer model
        utils.timer.is_running = data['active']
        utils.timer.duration = 60 * data['minutes'] + data['seconds']
        if(data['active']):
            utils.timer.start()

        m,s = utils.timer.get_time()
        

        # Update every frontend
        await self.channel_layer.group_send(
            "timer",
            {
                'type': 'timer_message',
                'active': data['active'],
                'minutes': m,
                'seconds': s,
            }
        )

    # Receive message from room group
    async def timer_message(self, event):
        m,s = utils.timer.get_time()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'active': event['active'],
                'minutes': event['minutes'],
                'seconds': event['seconds'],
        }))
