#!/usr/bin/env python

x,y,z = 15,10,5
print "x,y,z =", x,y,z
if x < y:
  if x < z: print "x is least"
  else: print "z is least"
else: print "y is least"
