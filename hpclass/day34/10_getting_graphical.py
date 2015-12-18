# Example of using Matplotlib to graph

import csv
import matplotlib.pyplot as plt

data_file = 'data.csv'

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

print 'distance = %s' % distance

# fig = plt.figure()
# fig.add_subplot(111)

# fig.title('Power vs. Time')
# fig.xlabel('Time (s)')

plt.plot(time, P_total, label='Total')
plt.savefig('PowerGraph.png')
plt.show() # shows the graph

# TODO:
#   - Create a graph of Total Power vs. Time
#   - Save as PowerGraph.png
#   - Add title, labels
#   - Add Latent Power vs. Time
#   - Add legend

# Bonus:
#   - use plt.ylim()
#   - use plt.scale()


    
