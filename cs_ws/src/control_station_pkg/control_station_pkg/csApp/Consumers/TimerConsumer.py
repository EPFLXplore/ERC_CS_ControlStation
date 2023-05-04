import json
# from channels.generic.websocket import AsyncWebsocketConsumer

from .RoverConsumer import RoverConsumer
import MVC_node.models.utils as utils


"""

Data format :
{

    'launch': bool,
    'hours': int,
    'minutes': int,
    'seconds': int,

}

"""


class TimerConsumer(RoverConsumer):
    
    async def connect(self):
        self.room_group_name = 'tab_timer'
        print("connect to timer consumer")
        # Join tab group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send(text_data=json.dumps({"launch":utils.timer.is_running,
                                        "duration":utils.timer.duration,}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        #update timer model
        utils.timer.is_running = text_data['launch']
        utils.timer.duration = text_data['duration']

        # Update every frontend
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'broadcast',
                'launch': utils.timer.is_running,
                'duration': utils.timer.duration,
            }
        )

    # Receive message from room group
    async def broadcast(self, event):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'launch': utils.timer.is_running,
            'duration': utils.timer.duration,
        }))
