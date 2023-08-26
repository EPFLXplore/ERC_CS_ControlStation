import numpy as np

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):

        channel_layer = get_channel_layer()
        
        #SCIENCE DATA
        self.mass = [0,0]
        self.candidates = []
        self.spectrometer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.spectrometer_closest_candidate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.npk_sensor = [0,0,0]
        self.four_in_one = [0,0,0,0]

        #SCIENCE DRILL
        self.state = 0
        self.potentiometers = []
        self.led_confirm = []
        self.hd_volmeter = []
        self.hd_laser = []


        # array of infos coming from the SC (in the form of Strings)
        self.__info = []

        # command we'd like the science bay to execute (in the case of a tube-specific operation: op + tube)
        self.__cmd = -1

    def UpdateScienceDataSocket(self):
        async_to_sync(self.channel_layer.group_send)("science_data", 
            {
                "type": "science_data_message",
                'mass' : self.mass,
                #'candidates' : self.candidates,
                'spectrometer' : self.spectrometer,
                'spectrometer_closest_candidate' : self.spectrometer_closest_candidate,
                'npk_sensor' : self.npk_sensor,
                'four_in_one' : self.four_in_one,
            })


    def UpdateScienceDrillSocket(self):
        async_to_sync(self.channel_layer.group_send)("science_drill", 
            {
                "type": "science_drill_message",

            })