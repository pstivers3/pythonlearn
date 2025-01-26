#!/usr/bin/env python3

f = open('testfile', 'w')
a = 2
b = 1.03
print("%3d %0.2f" % (a, b), file=f) # one way to write to file 
f.write("%3d %0.2f\n" % (a,b)) # another way to write to file
f.close()
