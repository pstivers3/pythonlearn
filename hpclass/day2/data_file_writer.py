#!/usr/bin/env python

import math
import circle_functions

# define a function
def circumference(given_radius):
  """
  returns the circumference from a raduus
  """
  value = 2.0 * math.pi * given_radius
  return value

# this is where the main code starts
f = open('data.csv', 'w')
line = 'radius, circ, area\n'
f.write(line)
for radius in range(1, 50):
  circ = circumference(radius)
  area = circle_functions.area(radius) 
  line = "%.2f, %.2f, %.2f\n" % (radius, circ, area)
  f.write(line)

f.close()

