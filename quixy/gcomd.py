#!/usr/bin/env python

def gcomd(a,b):
    if isinstance(a, int) and isinstance(b, int):
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a

print gcomd(44,20)

