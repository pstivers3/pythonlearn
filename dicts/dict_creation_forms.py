#!/usr/bin/env python3

# traditional literal expression
d = {'k0':0}

# assign by keys dynamically. Updates the dictionary
d['k1'] = 'v1' 
print(d)

# dict keyword argument. Replaces the dictionary
d = dict(k2 = 2, k3 = 3)
print(d)

# dict key/value tuples. Replaces the dictionary
d = dict([('k4', 'v4'), ('k5', 'v5')])
print(d)

# dict keyword argument. Updates the dictionary
d.update(dict(k6 = 6, k7 = 7))
print(d)
