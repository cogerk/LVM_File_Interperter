"""
Written by: Kathryn Cogert
For: Winkler Lab
Date: 01/05/2016
Purpose: Take lvm file that was saved as a txt and parse data into xls
"""
import pandas as pd

# Open files and define empty lists.
f = open('run1.txt', 'r')
time = list()
amp = list()

# Go through lines of file 
for line in f:
    # Find lines with timestamps, dataclean, and add to list
    if 'Time,' in line and 'X' not in line:
        ts = line[5:-3]
        time.append(str(ts))
    # Find lines with amp measurements, dataclean, and add to list
    if '0.000000,' in line:
        val = line[9:-2]
        amp.append(val)
#The first timestamp had no value attached to it, so dataclean that out
time.pop(0)

#Put in dataframe and write to CSV
DF = pd.DataFrame({'Timestamp': time,
                   '4-20 mA Reading, A': amp
                   })
DF.set_index(['Timestamp'], inplace=True)
DF.to_csv('run1.csv')
print DF
