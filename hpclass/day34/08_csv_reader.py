# Example of using csv.reader() function to data.

import csv
import matplotlib.pyplot as plt

distance = []
time = []

data_file = 'power.csv'

f = open(data_file, 'r')

# skip the first 3 lines
for item in range(3):
  toss = f.readline()

# store first column in list distance
# store second column in list time
for line in csv.reader(f, skipinitialspace=True):
  distance.append(float(line[0]))
  time.append(float(line[1]))   
  print line
for item in distance:
  print item
for item in time:
  print item 
f.close()


# TODO:
#   - Skip header lines.
#   - Create empy lists for data
#   - append data into separate lists
