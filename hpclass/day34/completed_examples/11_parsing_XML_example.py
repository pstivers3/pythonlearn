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


data = element.childNodes[0].data.strip()
units = element.getAttribute('units').strip()

print 'tagName = %s' % tagName
print 'data = %s' % data
print 'units = %s' % units


# Bonus:
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
    data, units = getXML(sim_folder, sim_id, 'topsideAirVelocity')
    print '%s, %s, %s' % (sim_id, data, units)


