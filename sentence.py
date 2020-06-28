##########################################################################################
################################### Imports ##############################################

import os    # Module to create file paths across operating systems
import csv   # Module to read CSV files
import time  # Track time for program to execute
import re    # https://docs.python.org/3/library/re.html

start_time = time.process_time()  # Track Time (start)

##########################################################################################
######################### Data Extract / Create Dict #####################################

csvpath1 = os.path.join('raw_data', 'paragraph_1.txt')
csvpath2 = os.path.join('raw_data', 'paragraph_2.txt')

with open(csvpath1) as csvfile1, open(csvpath2) as csvfile2:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    csvreader2 = csv.reader(csvfile2, delimiter=',')

    # Header row:  Voter ID,County,Candidate
    header_row1 = next(csvreader1)
    header_row2 = next(csvreader2)

    print(header_row1)
    print(header_row2)


    # # 
    # for row in csvreader: