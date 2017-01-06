"""
Written by: Kathryn Cogert
For: Winkler Lab
Date: 01/05/2016
Purpose: Take lvm file that was saved as a txt and parse data into xls
"""
import pandas as pd

f = open('run1.txt', 'r')
time = list()
amp = list()
for line in f:
    if 'Time,' in line and 'X' not in line:
        ts = line[5:-3]

        time.append(str(ts))
    if '0.000000,' in line:
        val = line[9:-2]
        amp.append(val)
time.pop(0)

DF = pd.DataFrame({'Timestamp': time,
                   '4-20 mA Reading, A': amp
                   })
DF.set_index(['Timestamp'], inplace=True)
DF.to_csv('run1.csv')
print DF