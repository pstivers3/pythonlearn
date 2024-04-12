#!/usr/bin/env python3

from columnar import columnar

vars_copy = dict(vars())
for var in vars_copy:
    columnar
    print(columnar('%s: %s' % (var, vars_copy[var])))
