# needs work

import os

f = open('data.html', 'w')
sim_folder = 'sim_files'
f.write('<tr>')
f.write('<th>Sim ID</th>')
f.write('<th>Data</th>')
f.write('<th>Units</th>')
f.write('<tr>')

for sim_id in os.listdir(os.path.join(os.getcwd(), sim_folder)):
  data, units = getXML(sim_folder, sim_id, tagName)
  f.write('<th>%s</th>\n' % sim_id)
  f.write('<th>%s</th>') % data
  f.write('<th>%s</th>') % units
  f.write('<tr>\n')
f.write('<table>\n')
#f.write('<A href="data.txt"> HOT PROPERTY </A>
# f.write('<A href="PoserGraph.png"><IMG src="PowerGraph href="PoserGraph.png"><IMG src="PowerGraph.png

f.close()

