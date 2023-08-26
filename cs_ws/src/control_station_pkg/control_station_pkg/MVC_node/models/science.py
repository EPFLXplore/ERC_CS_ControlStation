import numpy as np

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):

        self.channel_layer = get_channel_layer()
        
        #SCIENCE DATA
        self.mass = [0,0]
        self.candidates = []
        self.spectrometer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.spectrometer_closest_candidate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.npk_sensor = [0,0,0]
        self.four_in_one = [0,0,0,0]

        #SCIENCE DRILL
        self.state = 0
        self.motors_pos = [0,0]
        self.motors_speed = [0,0,0]
        self.motors_currents = [0,0,0]
        self.limit_switches = [0,0,0,0]


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
                'mass' : [self.mass[0], self.mass[1]],
                'spectrometer' : [self.spectrometer[0], self.spectrometer[1], self.spectrometer[2], self.spectrometer[3], self.spectrometer[4], self.spectrometer[5], self.spectrometer[6], self.spectrometer[7], self.spectrometer[8], self.spectrometer[9], self.spectrometer[10], self.spectrometer[11], self.spectrometer[12], self.spectrometer[13], self.spectrometer[14], self.spectrometer[15], self.spectrometer[16]],
                'spectrometer_closest_candidate' : [self.spectrometer_closest_candidate[16], self.spectrometer_closest_candidate[15], self.spectrometer_closest_candidate[14], self.spectrometer_closest_candidate[13], self.spectrometer_closest_candidate[12], self.spectrometer_closest_candidate[11], self.spectrometer_closest_candidate[10], self.spectrometer_closest_candidate[9], self.spectrometer_closest_candidate[8], self.spectrometer_closest_candidate[7], self.spectrometer_closest_candidate[6], self.spectrometer_closest_candidate[5], self.spectrometer_closest_candidate[4], self.spectrometer_closest_candidate[3], self.spectrometer_closest_candidate[2], self.spectrometer_closest_candidate[1], self.spectrometer_closest_candidate[0]],
                'npk_sensor' : [self.npk_sensor[0], self.npk_sensor[1], self.npk_sensor[2]],
                'candidates' : self.candidates,
                'four_in_one' : [self.four_in_one[0], self.four_in_one[1], self.four_in_one[2], self.four_in_one[3]],
            })
                

    def UpdateScienceDrillSocket(self):
        async_to_sync(self.channel_layer.group_send)("science_drill", 
            {
                "type": "science_drill_message",
                'state' : self.state,
                'motors_pos' : [self.motors_pos[0], self.motors_pos[1]],
                'motors_speed' : [self.motors_speed[0], self.motors_speed[1], self.motors_speed[2]],
                'motors_currents' : [self.motors_currents[0], self.motors_currents[1], self.motors_currents[2]],
                'limit_switches' : [self.limit_switches[0], self.limit_switches[1], self.limit_switches[2], self.limit_switches[3]],

            })
        
    def FindClosestCandidate(self):
        #TODO
        #mettre le code de science ici
        #update self.spectrometer_closest_candidate
        #update self.candidates
        self.spectrometer_closest_candidate = self.spectrometer
        pass