#!/usr/bin/python

# Example of parsing text from a file.
# Value 'TU' is the dryer topside air temperature.


import matplotlib.pyplot as plt
import numpy as np
import os, sys


data_file = 'vapor.out'

f = open(data_file, 'r')

for line in f.readlines():
  if 'TU' in line:
    tuline = line
    value = tuline.split()[2]
    try:
      value = float(value)
    except:
      pass
    break
  print line,
print tuline,
print value,


# TODO:
#   - Run example to see what data 'line' contains.
#   - Figure out how to capture line containing 'TU ='.
#   - Figure how to split line to get value into variable.
    
# Bonus:
#   - Modify to get data from 'sim_files/lr0/vapor.out'
#   - Create function taking sim_id ('lr0') and returning TU.
#   - Use "if __name__ == '__main__':" and make a call
#     to the function if run from script instead of imported.

    
