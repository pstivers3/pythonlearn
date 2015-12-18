#!/usr/bin/env python2.7

def f(x,y):
    print x, y

f(1,2)

def fea(x,y,*args):
   print x, y, args

fea(1,2,3,4,5)

fea(x=3,y=4)

def fkwa(x,y,*args,**kwargs):
    print x, y, args, kwargs

fkwa(1,2,3,4,5,z=6,w=7)
fkwa(1,2)
