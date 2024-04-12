#!/usr/bin/env python3

vars_copy = dict(vars())

max_key_len = max(len(key) for key in vars_copy.keys())
for key, value in vars_copy.items():
    print(f'{key:<{max_key_len}} : {value}')

    # simpler print statement, but lacking  variable column width for keys
    # print('%-20s: %s' % (var, vars_copy[var]))
