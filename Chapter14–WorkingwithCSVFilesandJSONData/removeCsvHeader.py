#! /usr/bin/python3.5


"""

Author: Samrat Banerjee
Dated: 07/09/2018
Description: Project: Removes the header from all CSV files in the current working directory

"""

import os,csv

os.makedirs('headerRemoved',exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
        
    
