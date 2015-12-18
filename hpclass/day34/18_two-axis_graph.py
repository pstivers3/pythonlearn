# Example of two-y-axis graph

import csv
import matplotlib.pyplot as plt
import os, sys

sim_folder = 'sim_files'
sim_id = 'lr0'
data_file = 'vapor.csv'
file_path = os.path.join(os.getcwd(), sim_folder,
                         sim_id, data_file)

# create empty lists (arrays)
distance = []
time = []
temp = []
pct = []
rate = []

f = open(file_path, 'r')

# skip header rows
for item in range(3):
    f.readline()

for line in csv.reader(f, skipinitialspace=True):
    print line
    distance.append(line[0])
    time.append(line[1])
    temp.append(line[2])
    pct.append(line[3])
    rate.append(line[4])

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

title = 'Temperature and Vapor vs. Time'
plt.title(title, fontsize='x-large', color='b')
plt1 = ax.plot(time, temp, '-b', label='Temperature')
plt2 = ax2.plot(time, pct, '-r', label='Percent')
plts = plt1 + plt2
labs = [l.get_label() for l in plts]

ax.set_xlabel('Time (s)')
ax.set_ylabel('Temp (C)', color='blue', fontsize='large')
ax2.set_ylabel('Percent (%)', color='red', fontsize='large')

ax.grid(True)
ax.legend(plts, labs, loc='best')

fig.savefig('Two-axis_graph.png')
plt.show()


    
