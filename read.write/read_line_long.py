#!/usr/bin/env python
file = 'words.txt'
f = open(file)             # Returns a file object
line = f.readline()        # Invokes readline() method on file
while line:
  print line,              # trailing ',' omits newline character
  line = f.readline()
f.close()
