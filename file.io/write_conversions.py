#!/usr/bin/env python3

f = open('conversions.txt', 'w')
X, Y, Z = 62, 63, 64                       # Native Python objects
S = 'Text'                                 # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')              # Create output text file
F.write(S + '\n')                          # Terminate lines with \n
F.write(f'{X},{Y},{Z}\n')                  # Convert numbers to strings
F.write(str(L) + '$' + str(D) + '\n')      # Convert and separate with $
F.close()

