#!/usr/bin/env python2.7

import argparse, sys # argparse is a module
# usage() is my own function to print usage and example
def usage():
    print "usage:", sys.argv[0], "   "
    print "example:", sys.argv[0], "   "
# ArgumentParser is a class
# parser is an object
parser = argparse.ArgumentParser(description='experiment with argparse')
# add_argument() is a method. first positional argument is stored in variable x
parser.add_argument("x")
# second positional argument is stored in variable y
parser.add_argument("y")
# parse_args() is a method that returns the Namespace dictionary of arguments
args = parser.parse_args()
print args
print args.x
print args.y
