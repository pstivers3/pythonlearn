#!/usr/bin/env python

import sys                       # Load the sys module
usage = '\nusage: ' + sys.argv[0] + ' float.list\n'

# if not one command line argument, print usage and exit
if len(sys.argv) != 2: 
  print usage 
  raise SystemExit(1)

# if command line argument is 'help' print usage and exit
if sys.argv[1] == 'help':
  print usage 
  raise SystemExit(1)

# Convert all of the input values from strings to floats
fvalues = [float(line) for line in open(sys.argv[1])]

# Print min and max values
print "The minimum value is ", min(fvalues)
print "The maximum value is ", max(fvalues)
