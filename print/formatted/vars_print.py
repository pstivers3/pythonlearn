#!/usr/bin/env python3

vars_copy = dict(vars())

max_key_len = max(len(key) for key in vars_copy.keys())
for key, value in vars_copy.items():
    print(f'{key:<{max_key_len}} : {value}')

    # Another way. Wildcard pulls from fist value in the tupple. 
    # print('%-*s : %s' % (max_key_len, key, value))
