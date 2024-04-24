#!/usr/bin/env python3

m = {'a': 1, 'b':2, 'c': 3, 'd':2}

# three ways to check for missing key
# one
if 'e' in m:
    print(m['e'])
else:
    print(0)

# two
try:
    print(m['e'])
except KeyError:
    print(0)

# three
print(m.get('e', 0))

# get an existing key
print(m.get('a', 0))
