#!/usr/bin/env python3

# first way
print(open('../files/words.txt').read())

# iterator way 
for line in open('../files/words.txt'):
  print(line, end='') 

print()

# loop way
file = '../files/words.txt'
f = open(file)             # Returns a file object
line = f.readline()        # Invokes readline() method on file
while line:
  print(line, end='')      # end='' prevents extra new line
  line = f.readline()
f.close()

