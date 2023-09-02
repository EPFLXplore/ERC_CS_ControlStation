import numpy as np
import pandas as pd
import os

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

    def load_spectrum(self, filename):
        return pd.read_csv(filename)

    def calculate_rmsd(self, spectrum1, spectrum2):
        """Calculate the RMSD between two spectra."""
        return np.sqrt(((spectrum1 - spectrum2) ** 2).mean())

    def identify_mineral(self, measured_spectrum_file, database_dir):
        """Identify mineral by comparing measured spectrum with database."""
        
        # Load measured spectrum
        measured_spectrum = self.load_spectrum(measured_spectrum_file)['reflectance']
        
        # A list of tuples, each containing filename and its RMSD. Initialized with high values.
        top_matches = [(None, float('inf')), (None, float('inf')), (None, float('inf'))]
        
        # Go through each file in the database directory
        for filename in os.listdir(database_dir):
            if filename.endswith('.csv'):
                filepath = os.path.join(database_dir, filename)
                database_spectrum = self.load_spectrum(filepath)['reflectance']
                
                # Calculate RMSD between measured spectrum and this database spectrum
                rmsd = self.calculate_rmsd(measured_spectrum, database_spectrum)
                
                # Check if this RMSD is among the top three
                if rmsd < top_matches[2][1]:  # Compare with the highest RMSD in the current top 3
                    top_matches[2] = (filename, rmsd)
                    top_matches.sort(key=lambda x: x[1])  # Sort based on RMSD
        
        # Convert RMSD values to relative percentage difference
        total_rmsd = sum([x[1] for x in top_matches])
        percentages_diff = [(x[0], 100 * x[1] / total_rmsd) for x in top_matches]
        
        # Calculate similarity as 100% minus the percentage difference
        percentages_similarity = [(x[0], 100 - x[1]) for x in percentages_diff]
        
        return percentages_similarity
    
    def compare(self, measured_file):
        """ Compare measured spectrum with database and print results.

        Args: 
            measured_file (str): Path to the measured spectrum file.
        """
        database_directory = '/data/Spectroscopy_database/'
        identified_minerals = self.identify_mineral(measured_file, database_directory)

        best_candidate = None
        best_candidate_percentage = 0
        for mineral, percentage in identified_minerals:
            if percentage > best_candidate_percentage:
                best_candidate = mineral
                best_candidate_percentage = percentage
        
        return best_candidate, best_candidate_percentage

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
        #update self.spectrometer and create the csv file

        self.spectrometer_closest_candidate = self.spectrometer
        pass