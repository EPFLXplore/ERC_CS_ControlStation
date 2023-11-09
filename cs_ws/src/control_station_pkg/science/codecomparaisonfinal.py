import pandas as pd
import numpy as np
import os

def load_spectrum(filename):
    
    return pd.read_csv(filename)

def calculate_rmsd(spectrum1, spectrum2):
    """Calculate the RMSD between two spectra."""
    return np.sqrt(((spectrum1 - spectrum2) ** 2).mean())

def identify_mineral(measured_spectrum_file, database_dir):
    """Identify mineral by comparing measured spectrum with database."""
    
    # Load measured spectrum
    measured_spectrum = load_spectrum(measured_spectrum_file)['reflectance']
    
    # A list of tuples, each containing filename and its RMSD. Initialized with high values.
    top_matches = [(None, float('inf')), (None, float('inf')), (None, float('inf'))]
    
    # Go through each file in the database directory
    for filename in os.listdir(database_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(database_dir, filename)
            database_spectrum = load_spectrum(filepath)['reflectance']
            
            # Calculate RMSD between measured spectrum and this database spectrum
            rmsd = calculate_rmsd(measured_spectrum, database_spectrum)
            
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

def compare():
    measured_file = '/Users/alexandrejaczynski/Desktop/testmathieu/testmathieu.csv'
    database_directory = '/Users/alexandrejaczynski/Desktop/testmathieu/datasetfinalxxxxx'
    identified_minerals = identify_mineral(measured_file, database_directory)

    for mineral, percentage in identified_minerals:
        print(f"{mineral}: {percentage:.2f}% similarity")

if __name__ == '__main__':
    compare()
