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

    # # Header row:  Not applicable
    # header_row1 = next(csvreader1)
    # header_row2 = next(csvreader2)
    # print(header_row1)
    # print(header_row2)

    paragraph=[]
    sentences=[]
    words=[]
    capital_words=[]
    letters=[]


    files = [csvreader1, csvreader2]

    for page in files:
        for row in page:
            if not row:
                continue
            else:
                paragraph.append(row)
                # need to merge all paragraphs 

    for item in range(len(paragraph)):
        for items in paragraph[item]:
            sentences.append(re.split(r"(?<=[.!?]) +", items))

    for item in range(len(sentences)):
        for items in sentences[item]:
            words.append(re.split(r"\W+", items))    

    for item in range(len(words)):
        for items in words[item]:
            letters.append(re.split(r"([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\)", items)) 


    print(len(letters))


# 
# print(sentences)    