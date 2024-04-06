#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("usage:", sys.argv[0],"<argument> [additinal arguments]")
    sys.exit()
    
print("the filename is:", sys.argv[0])  #  script name
print("\nthe arguments are:")
for arg in sys.argv[1:]: # slice to omit the filename 
    print(arg)

print("\nthe total number of args not counting the filename is:", len(sys.argv[1:]))

