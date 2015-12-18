# Example of parsing text from a file.
# Value 'TU' is the dryer topside air temperature.


import matplotlib.pyplot as plt
import numpy as np
import os, sys


data_file = 'vapor.out'

f = open(data_file, 'r')


# TODO:
#   - Run example to see what data 'line' contains.
#   - Figure out how to capture line containing 'TU ='.
#   - Figure how to split line to get value into variable.
    
# Bonus:
#   - Modify to get data from 'sim_files/lr0/vapor.out'
#   - Create function taking sim_id ('lr0') and returning TU.
#   - Use "if __name__ == '__main__':" and make a call
#     to the function if run from script instead of imported.


for line in f.readlines():
    if 'TU = ' in line:
        TU = line.strip().split()[2]
        break

print 'TU = %s' % TU  


# Bonus:
def getTU(sim_folder, sim_id):
    ''' get TU from vapor.out in folder sim_id '''
    data_file = 'vapor.out'
    file_path = os.path.join(os.getcwd(), sim_folder,
                             sim_id, data_file)
    f = open(file_path, 'r')
    for line in f.readlines():
        if 'TU = ' in line:
            TU = line.strip().split()[2]
            break
    return TU


if __name__ == '__main__':
    sim_folder = 'sim_files'
    sim_id = 'lr0'
    #TU = getTU(sim_folder, sim_id)
    #print 'TU = %s' % TU 
