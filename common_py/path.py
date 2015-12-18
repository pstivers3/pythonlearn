#!/usr/bin/env python2.7

import os

print os.path.realpath(__file__)
print os.path.realpath(os.path.join(__file__, '../..'))
print os.path.realpath('./path.py/../..')
print os.path.join(__file__, '../..')
