#!/usr/bin/env python3

# Your program should take as input the height H of the bow tie, where H is an odd positive integer greater than or equal to 5. 
# A bow tie with H rows (and 2H columns) should then be printed using the pattern shown below. You may assume that all input data will be valid.

# input = 5

#  *        *
#  ***    ***
#  **********
#  ***    ***
#  *        *

# input = 7

#  *            *
#  ***        ***
#  *****    *****
#  **************
#  *****    *****
#  ***        ***
#  *            *

from __future__ import print_function

h = 7
w = 2*h
half = (h-1)//2
print () 

x = 1
for n in range(0,half): 
    print ('*' * x, end='')
    spaces = w - 2*x
    print (' ' * spaces, end='')
    print ('*' * x)
    x += 2

print ('*' * w, end ='')
print () 

x = (w-4)//2 
for n in range(0,half): 
    print ('*' * x, end='')
    spaces = w - 2*x
    print (' ' * spaces, end='')
    print ('*' * x)
    x -= 2

print()
