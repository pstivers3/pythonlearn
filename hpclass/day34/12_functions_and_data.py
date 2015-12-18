# Example of function and use of "__name__ == '__main__'.

import matplotlib.pyplot as plt
import numpy as np
import os, sys
from xml.dom import minidom


data_file = 'simulation_data.xml'
tagName = 'topsideAirVelocity'

xmldoc = minidom.parse(data_file)
element = xmldoc.getElementsByTagName(tagName)[0]
print 'element for "%s":\n\n%s' % (tagName, element.toxml())

data = element.childNodes[0].data.strip()
units = element.getAttribute('units').strip()

print 'tagName = %s' % tagName
print 'data = %s' % data
print 'units = %s' % units


# TODO:
#   - Turn XML code into "getXML()" function
#     which returns data and units.
#   - Use "if __name__ == '__main__':" to call function.
#   - Get data from 'lr0' directory file.

# Bonus:
#   - Use os module to get a list of directories in "sim_files".



