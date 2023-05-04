import json
import random
# from channels.generic.websocket import AsyncWebsocketConsumer

from .InfoRoverConsumer import RoverConsumer
from asgiref.sync import sync_to_async


""""

Data format:
{

    'State' : ,
    'hd_mode' : ,
    'joint_pos' : joint_position,
    'joint_vel' : joint_velocity,
    'detected_elems' : list,


"""


class HdAutoConsumer(RoverConsumer):
    
    async def connect(self):

        current_session_date = await sync_to_async(self.scope['session'].load)()
        self.scope['session'].update(current_session_date)
        
        # if 'userID' in self.scope['session']:
        #     print("already connected : " + str(self.scope['session']['userID']))
        # else:
            #self.scope['session']['userID'] = random.randint(0, 100)
            #print("first connection : " + str(self.scope['session'].session_key))
        try :
            print("exist deja : " + str(self.scope['session']['userID']))
        except :
            self.scope['session']['userID'] = random.randint(0, 100)
            print("exist pas : " + str(self.scope['session']['userID']))

        self.scope['session'].update(current_session_date)
        await sync_to_async(self.scope['session'].save)()

        # #self.scope['session'].save()
        self.tab_name = 'handlingdevice'
        self.tab_group_name = 'tab_%s' % self.tab_name

        # Join tab group
        await self.channel_layer.group_add(
            self.tab_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print("disconneted")
        del self.scope['session']
        # Leave tab group
        await self.channel_layer.group_discard(
            self.tab_group_name,
            self.channel_name
        )



    # Receive message from WebSocket
    async def receive(self, text_data):
        print("session key : " + str(self.scope['session']['userID']))

        text_data_json = json.loads(text_data)
        joint_position = text_data_json['joint_pos']
        joint_velocity = text_data_json['joint_vel']
        detected_elements = text_data_json['detected_elems']
        tof            = text_data_json['tof']

        # Send message to room group
        await self.channel_layer.group_send(
            self.tab_group_name,
            {
                'type': 'topic_message',
                'joint_pos': joint_position,
                'joint_vel': joint_velocity,
                'detected_elems': detected_elements,
                'tof'      : tof
            }
        )

    # Receive message from room group
    async def topic_message(self, event):
        print("topic message:")
        joint_position = event['joint_pos']
        joint_velocity = event['joint_vel']
        detected_elements = event['detected_elems']
        tof            = event['tof']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'joint_pos': joint_position,
            'joint_vel': joint_velocity,
            'detected_elems': detected_elements,
            'tof'      : tof
        }))
