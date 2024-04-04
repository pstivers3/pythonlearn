#!/usr/bin/env python3

file = 'words.txt'
f = open(file)             # Returns a file object
line = f.readline()        # Invokes readline() method on file
while line:
  print(line, end='')      # end='' prevents extra new line
  line = f.readline()
f.close()
