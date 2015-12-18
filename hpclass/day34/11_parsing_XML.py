# Open 'simulation_data.xml' and parse to get
# value for 'topsideAirVelocity'.

import os, sys
from xml.dom import minidom

data_file = 'simulation_data.xml'
tagName = 'topsideAirVelocity'

xmldoc = minidom.parse(data_file)
element = xmldoc.getElementsByTagName(tagName)[0]
print 'element for "%s":\n\n%s' % (tagName, element.toxml())

# TODO:
#   - run example to see what data 'element' contains.
#   - Look at http://docs.python.org/library/xml.dom.html
#   check values for the following:
#       - element.childNodes[0].data
#       - element.getAttributes('units')

# Bonus:
#   - Turn into function.
#   - Modify to get data from 'sim_files/lr0/simulation_data.xml'



