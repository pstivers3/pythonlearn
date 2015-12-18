#!/usr/bin/env python

f = open('data.csv', 'r')
# index down one line because the file has a text header
f.readline()
for line in f:
  r, c, a = line.strip('\n').split(',')
  print 'Radius=%f :Circumfrance=%f :Area=%f' % (float(r), float(c), float(a))
f.close()

