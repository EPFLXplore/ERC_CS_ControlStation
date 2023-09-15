import numpy as np
import pandas as pd
from pathlib import Path

import os
import logging

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):

        self.channel_layer = get_channel_layer()
        
        #SCIENCE DATA
        self.mass = [0, 0, 0, 0]
        self.candidates = []

        self.spectrometer_list = [] #list of spectrometers
        self.spectrometer_mean = []
        self.npk_sensor = [0,0,0]
        self.four_in_one = [0,0,0,0]
        self.spectrometer_closest_candidate = [0 for i in range(15)]
        self.wavelengths_input = [410,435,460,485,510,535,560,585,610,645,680,705,730,760,810,860,900,940]
        self.wavelengths_output = [460,480,500,520,540,660,680,700,720,740,860,880,900,920,940]
        self.wavelength_interpolate_index = [2,3,4,5,6,8,9,11,13]

        self.nb_measures = 0

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

    def load_spectrum_from_file(self, filename):
        """Load the top line from a file and return it as a list of numbers."""

        text = np.loadtxt(filename, skiprows=1, delimiter=',')
        print(text)
        logging.info("text: " + str(text))

        return [float(value) for value in text]

    def calculate_rmsd(self, spectrum1, spectrum2):
        """Calculate the RMSD between the measured spectra and the databse ."""
        return np.sqrt(((spectrum1 - spectrum2) ** 2).mean())

    def identify_mineral(self, measured_spectrum_file, database_dir):
        """main comparaison function """
        
        # Loads the measured spectrum from the measured_spectrum_file
        measured_spectrum_list = self.load_spectrum_from_file(measured_spectrum_file)
        measured_spectrum = pd.Series(measured_spectrum_list, name='reflectance')
        
        # A list of tuples, each containing filename and its RMSD. Initialized with high values.
        top_matches = [(None, float('inf')), (None, float('inf')), (None, float('inf'))]
        
        # this goes through each file in the directory to check 
        for filename in os.listdir(database_dir):
            if filename.endswith('.csv'):
                filepath = os.path.join(database_dir, filename)
                database_spectrum = pd.read_csv(filepath)['Calibrated reflectance']
                
                # Calculate RMSD between measured spectrum and this database spectrum
                rmsd = self.calculate_rmsd(measured_spectrum, database_spectrum)
                
                # Check if this RMSD is among the top three
                if rmsd < top_matches[2][1]:  # Compare with the highest RMSD in the current top 3
                    top_matches[2] = (filename.split('.')[0], rmsd)
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
        database_directory = str(Path(__file__).parent.absolute()) + '/data/output-data/'
        identified_minerals = self.identify_mineral(measured_file, database_directory)

        # Return the list of candidates sorted by their percentage similarity
        return identified_minerals

    def transform_spectrometer(self, data):
        """Transform the spectrometer data to the wavelength of the science bay"""

        new_data = [0 for i in range(15)]
        new_data[0] = data[2]
        new_data[1] = data[3]
        new_data[6] = data[10]
        new_data[7] = data[11]
        new_data[9] = data[15]
        new_data[11] = data[16]
        new_data[13] = data[17]

        # We now populate the rest of the array with interpolated values: [2,3,4,5,6,8,9,11,13]
        for i in range(2,15):
            if i in self.wavelength_interpolate_index:
                new_data[i] = np.interp(self.wavelengths_output[i], self.wavelengths_input, data)

        return new_data

    def reset_spectrometer(self):
        """Reset the spectrometer list"""
        self.spectrometer_list = []

    def mean_spectrometer(self):
        """Calculate the mean of the spectrum from the list of spectrometers"""
        self.spectrometer_mean = np.mean(self.spectrometer_list, axis=0)

    def store_spectrum(self):
        """Store the spectrum in a file."""
        # Create a pandas dataframe combing self.wavelength and self.spectrometer_mean with titles 'wavelength' and 'reflectance'
        df = pd.DataFrame({'reflectance': self.spectrometer_mean})
        # Save the dataframe to a csv file
        path = str(Path(__file__).parent.absolute()) + '/data/spectrum.csv'
        df.to_csv(path, index=False)

            
    def FindClosestCandidate(self):
        path = str(Path(__file__).parent.absolute()) + '/data/spectrum.csv'
        similarities = self.compare(path) # list of names and similarities
        # format the similarites as "similarity %, name" with similarity a 2 decimal float
        self.candidates = [str(round(similarity[1], 2)) + '%, ' + similarity[0] for similarity in similarities]
        
        # We now load the spectrum of the closest candidate from the database
        path = str(Path(__file__).parent.absolute()) + '/data/output-data/'

        db_spectro = pd.read_csv(path + similarities[0][0] + '.csv')['Calibrated reflectance'].tolist()
        # We need to read db_spectro as a list and add leading zeros to match the length of the measured spectrum
        logging.info("db_spectro: " + str(db_spectro))
        self.spectrometer_closest_candidate = db_spectro

        print(similarities)

        pass
    
        

    def UpdateScienceDataSocket(self):
        async_to_sync(self.channel_layer.group_send)("science_data", 
            {
                "type": "science_data_message",
                'mass' : [str(self.mass[0]), str(self.mass[1])],
                'spectrometer' : [str(val) for val in self.spectrometer_mean],
                'spectrometer_closest_candidate' : [str(val) for val in self.spectrometer_closest_candidate],
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
