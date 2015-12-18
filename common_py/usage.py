#!/usr/bin/env python2.7

import sys

def usage():
    print "usage:", sys.argv[0], "<arg1> [-h | --help] [-b | --bbb <argb>] [-c | --ccc]"
    print "example:", sys.argv[0], "arg1 -a --bbb argb"
	
def main(argv):                         
    bbb= "argb"                 
    try:                                
        opts, args = getopt.getopt(argv, "ab:c", ["aaa", "bbb=", "ccc"]) 
    except getopt.GetoptError:           
        usage()
        sys.exit(2)
    for opt, arg in opts:                
        if opt in ("-h", "--help"):
            print "-h and --help!"
            usage()                     
            sys.exit()                  
        elif opt == '-c':                
            print "-c!"               
        elif opt in ("-b", "--bbb"): 
            print "-b and --bbb! and", argb            

