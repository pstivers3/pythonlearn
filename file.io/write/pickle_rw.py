#!/usr/bin/env python3

import pickle

d = {'a': 1, 'b': 2}
f = open('../files/datafile.pkl', 'wb+') # read, write, binary
pickle.dump(d, f)        # pickle almost any object to file
f.seek(0)                # move the file pointer back to first line 
print(pickle.load(f))    # load almost any object from file
f.close()
