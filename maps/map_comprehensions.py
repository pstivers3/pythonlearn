#!/usr/bin/env python3

d = {x: x*2 for x in range(5)}
print(d)

# find the keys/s that have a given value
m = {'a': 1, 'b':2, 'c': 3, 'd':2}
k = [key for (key,value) in m.items() if value == 2]
print(k)

# a second way
k = [key for key in m.keys() if m[key] == 2]
print(k)
