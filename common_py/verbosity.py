#!/usr/bin/env python2.7

def set_verbosity(verbosity):
    try:
        verbosity = int(verbosity)
    except:
        verbosity = 0

    if verbosity < 0:
        verbosity = 0
    elif verbosity > 4:
        verbosity = 4

    print verbosity

set_verbosity('boo')
set_verbosity(5)
set_verbosity(3)
