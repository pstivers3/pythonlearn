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


# TODO:
#   - Create a graph of Total Power vs. Time
#   - Save as PowerGraph.png
#   - Add title, labels
#   - Add Latent Power vs. Time
#   - Add legend

# Bonus:
#   - use plt.ylim()
#   - use plt.scale()


# create graph
title = 'Power vs. Time'
plt.title(title, fontsize='x-large', color='b')
plt.plot(time, P_latent, label='Latent')
plt.plot(time, P_web, label='Web')
plt.plot(time, P_total, label='Total')

plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.ylim(0, 12000)
plt.grid(True)
plt.legend(loc='best')
plt.yscale('log')

plt.savefig('PowerGraph.png')
plt.show()


    
