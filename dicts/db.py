#!/usr/bin/env python3

m = {'k1': 'v1',
       'k2': ['v21', 'v22'],
       'k3':  'v3',
       'k4': {'k41': 'v41', 'k42': 'v42'}}

# A list "database"
db = []
db.append(m)
# db.append(other)
print(db[0]['k2'])

# A dictionary "database"
db = {}
db['m'] = m 
# db['name'] = other
print(db['m']['k2'])
print(db['m']['k4']['k42'])
