# Example of iterating over multiple files.


import matplotlib.pyplot as plt
import numpy as np
import os, sys
from xml.dom import minidom


def getXML(sim_folder, sim_id, tagName):
    ''' get element tagName from simulation_data.xml
        return data, units '''
    data_file = 'simulation_data.xml'
    file_path = os.path.join(os.getcwd(), sim_folder, sim_id, data_file)
    xmldoc = minidom.parse(file_path)
    node = xmldoc.getElementsByTagName(tagName)[0]
    data = node.childNodes[0].data.strip()
    units = node.getAttribute('units').strip()
    info = node.getAttribute('info').strip()
    return data, units


if __name__ == '__main__':

    sim_folder = 'sim_files'
    sim_folder = 'sim_files'
    sim_id = 'lr0'
    tagName = 'topsideAirVelocity'
    data, units = getXML(sim_folder, sim_id, tagName)
    print '%s) %s = %s %s' % (sim_id, tagName, data, units)

    
    # TODO:
    #   - Us os module to get a list of directories in "sim_files" folder.
    #   - Iterate over dir_list, calling getXML() function and print
    #     values for each simulation.

    # Bonus:
    #   - Write data to csv or text file.
    #   - Learn about os.walk()



