# Example of writing HTML with python.

DEBUG = True

import os
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

    f = open('results.csv', 'w')

    f.write('sim, air velocity, air units\n')

    for sim_id in dir_list:
        if 'lr' in sim_id:
            data, units = getXML(sim_folder, sim_id, 'topsideAirVelocity')
            print '%s, %s, %s' % (sim_id, data, units)
            f.write('%s, %s, %s\n' % (sim_id, data, units))
    f.close()
    print 'results.csv created!'


    # TODO:
    #   - Open file to write to.
    #   - Use Python string formatting to write correct HTML for a table.
    #   - Close out file.

    # Bonus:
    #   - Use text parsing function we wrote to gather and write out
    #     TU values as well.
    #   - Write full HTML tags for the file. (<HTML><HEAD><BODY>, etc.)
    #   - Correct the formatting so HTML source is indeted!.
    #   - Add a link to data text file.
    #   - Insert link to graph!


    # open file and write inital HTML stuff
    f = open('results.html', 'w')
    f.write('<html>\n')
    f.write('<head></head>\n')
    f.write('<body>\n')
    f.write('Air Flow Results\n')
    f.write('<table border="1">\n')
    f.write('  <tr><th>sim</th><th>air flow</th><th>units</th></tr>\n')
    
    for sim_id in dir_list:
        if 'lr' in sim_id:
            f.write('  <tr>\n') # start of row
            data, units = getXML(sim_folder, sim_id, 'topsideAirVelocity')
            out_line = '    <td>%s</td><td>%s</td><td>%s</td>\n' % (sim_id, data, units)
            #print out_line
            f.write(out_line)
            f.write('  </tr>\n') # end of row
    f.write('</table>\n')
    f.write('<a href="results.csv">Results File</a>\n')
    f.write('<img src="PowerGraph.png" />\n')
    f.write('</body>\n')
    f.write('</html>\n')
    f.close()
    print 'results.html created!'

