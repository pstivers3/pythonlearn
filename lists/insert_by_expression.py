#!/usr/bin/env python3

l = [0, 1, 2, 3, 4, 5, 6, 7]
print(l)

# insert in front
l[:0] = [0, 0, 0]
print(l)

# clip the inserted objects
l[:3] = []
print(l)

# append in back
l[len(l):] = [0, 0, 0]
print(l)

# clip the appended objects 
l[-3:] = []
print(l)

