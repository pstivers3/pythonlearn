# Example of writing to text or csv file.


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
    sim_id = 'lr0'
    tagName = 'topsideAirVelocity'
    
    dir_list = os.listdir(os.path.join(os.getcwd(), sim_folder))
    print 'dir_list = %s' % dir_list

    for sim_id in dir_list:
        if 'lr' in sim_id:
            data, units = getXML(sim_folder, sim_id, 'topsideAirVelocity')
            print '%s, %s, %s' % (sim_id, data, units)


    # TODO:
    #   - Open file to write to.
    #   - Itterate over dir_list, calling getXML() function and write
    #     values for each simulation.
    #   - Close out file.

    # Bonus:
    #   - Use text parsing function we wrote to gather and write out
    #     TU values as well.


