#!/usr/bin/env python3

# first way
for line in open('words.txt'):
  print(line, end='') 

print()

# second way
file = 'words.txt'
f = open(file)             # Returns a file object
line = f.readline()        # Invokes readline() method on file
while line:
  print(line, end='')      # end='' prevents extra new line
  line = f.readline()
f.close()

