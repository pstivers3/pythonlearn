#!/usr/bin/env python

def print_matches(matchtext):
  print "Looking for", matchtext
  while True:
    line = (yield)       # Get a line of text
    if matchtext in line:
      print line

matcher = print_matches("python")
matcher.next()  # Advance to the first (yield)
matcher.send("Hello World")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close()  # Done with the matcher function call
