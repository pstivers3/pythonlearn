# Example of using csv.reader() function to data.

import csv
import matplotlib.pyplot as plt

data_file = 'power.csv'

f = open(data_file, 'r')

for line in csv.reader(f, skipinitialspace=True):
    print line

f.close()


# TODO:
#   - Skip header lines.
#   - Create empy lists for data
#   - append data into separate lists


# open file and skip header rows
f = open(data_file, 'r')
for item in range(3):
    f.readline()

# create empty lists (arrays)
distance = []
time = []
P_latent = []
P_web = []
P_total = []

# read each line and get data points
for line in csv.reader(f, skipinitialspace=True):
    #print line
    distance.append(line[0])
    time.append(line[1])
    P_latent.append(line[2])
    P_web.append(line[3])
    P_total.append(line[4])

# close file once done with it
f.close()
