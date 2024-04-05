#!/usr/bin/env python3

import sys

try:
    a=sys.argv[1]  # first argument
except IndexError:
    print("usage:", sys.argv[0],"<argument> [additinal arguments]")
else:
    print("\nthe filename is:", sys.argv[0])  #  script name
    print("the first arg is:", sys.argv[1], "\n")  # first argument
    print("the filename and all the args are:")
    for arg in sys.argv: # list all the args
        print(arg)

    print("the total number of args is: ", len(sys.argv)) # number of arguments

