#!/usr/bin/env python2.7

import sys

print "the script name is:", sys.argv[0]  #  script name
print "the first arg is:", sys.argv[1]  # first argument

print "the file name and all the args are:"
for arg in sys.argv: # list all the args
    print arg

print "the total number of args is: ", len(sys.argv) # number of arguments

