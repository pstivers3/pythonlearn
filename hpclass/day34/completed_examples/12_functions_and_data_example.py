# Example of function and use of "__name__ == '__main__'.

import matplotlib.pyplot as plt
import numpy as np
import os, sys
from xml.dom import minidom


# TODO:
#   - Turn XML code into "getXML()" function
#     which returns data and units.
#   - Use "if __name__ == '__main__':" to call function.
#   - Get data from 'lr0' directory file.

# Bonus:
#   - Modify to get data from 'sim_files/lr0/simulation_data.xml'


def getXML(sim_folder, sim_id, tagName):
    ''' get element tagName from simulation_data.xml return data, units '''
    data_file = 'simulation_data.xml'
    file_path = os.path.join(os.getcwd(), sim_folder, sim_id, data_file)
    xmldoc = minidom.parse(file_path)
    element = xmldoc.getElementsByTagName(tagName)[0]
    data = element.childNodes[0].data.strip()
    units = element.getAttribute('units').strip()
    info = element.getAttribute('info').strip()
    return data, units


if __name__ == '__main__':

    sim_folder = 'sim_files'
    sim_id = 'lr0'
    tagName = 'topsideAirVelocity'
    data, units = getXML(sim_folder, sim_id, tagName)
    print '%s) %s = %s %s' % (sim_id, tagName, data, units)


    # Bonus:
    dir_list = os.listdir(os.path.join(os.getcwd(), sim_folder))
    print 'dir_list = %s' % dir_list

