#!/usr/bin/env python3

file = '../files/words.txt'
f = open(file)
try:
    for line in f:
        print(line, end='')
finally:
    f.close()

