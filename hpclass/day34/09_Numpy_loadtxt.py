# Example of using Matplotlib to graph

import csv
import matplotlib.pyplot as plt
import numpy as np


data_file = 'data.csv'

if False: #this is the hard way
    
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

else: #this is the easy way

    # load data using np.loadtxt()
    distance, time, P_latent, P_web, \
              P_total = np.loadtxt(data_file, \
              delimiter = ',', skiprows=3, unpack=True)

print 'P_web:'
print P_web


# TODO:
#   - what data type is P_web?
#   - can you itterate over it?
#   - can you index P_web items?



    
