import os, sys

sim_folder = ''
base_dir = os.getcwd()
fileName = 'power.csv'

for (path, dirs, files) in os.walk(os.path.join(base_dir, sim_folder)):
  print 'path = %s' % path
  print 'dirs = %s' % dirs 
  print 'files = %s' % files
  print '\n'
  if fileName in files:
    print 'found %s in %s' % (fileName, path)
 
