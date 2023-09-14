from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Electronic:
    def __init__(self):

        self.channel_layer = get_channel_layer()

        self.can0 = []
        self.can1  = []
    
    def setStates(self, arr, can):
        if(can == 0):
            self.can0 = arr
        elif(can == 1):
            self.can1 = arr
        else:
            raise Exception("can must be 0 or 1")
        
        async_to_sync(self.channel_layer.group_send)("session", {"type": "broadcast",
                                                                'can0': self.can0,
                                                                'can1': self.can1,
                                                                })