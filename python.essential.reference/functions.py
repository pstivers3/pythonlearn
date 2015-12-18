#!/usr/local/bin/python 

def remainder(a,b):
    q = a // b  # // is truncating division
    r = a -q*b
    return r

def divide(a,b):
    q = a // b # if a and b are integers, q is an integer
    r = a - q*b
    return (q,r)

print divide (1456,33)
