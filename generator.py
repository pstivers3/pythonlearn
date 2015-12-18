#!/usr/bin/env python

def countdown(n):
  print "Counting down!"
  while n > 0:
    yield n       # Generate a value (n)
    n -= 1

c = countdown(5)
print c.next()
print c.next()

for i in countdown(5):
  print i

