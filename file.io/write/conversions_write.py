#!/usr/bin/env python3

X, Y, Z = 62, 63, 64                       # Native Python objects
S = 'Text'                                 # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

f = open('../files/conversions.txt', 'w')
f.write(S + '\n')                          # Terminate lines with \n
f.write(f'{X},{Y},{Z}\n')                  # Convert numbers to strings
f.write(str(L) + '$' + str(D) + '\n')      # Convert and separate with $
f.close()

