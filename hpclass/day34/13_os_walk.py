# brief os.walk() example


import os, sys

sim_folder = 'sim_files'
base_dir = os.getcwd()


for (path, dirs, files) in os.walk(os.path.join(base_dir, sim_folder)):
    print 'path = %s' % path
    print 'dirs = %s' % dirs
    print 'files = %s' % files
    print '\n'




                
                
            
    
