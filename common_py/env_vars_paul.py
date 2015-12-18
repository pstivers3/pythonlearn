#!/usr/bin/env python2.7

import os
# from subprocess import Popen

def print_vars_ab():
    print "A =", env_vars['A']
    print "B =", env_vars['B']
    print "$A =", os.popen("printf %s $A").read() #pipe open
    print "$B =", os.popen("printf %s $B").read()

def clear_env_vars(): 
    for var in env_vars.iterkeys(): # iterate over the keys
        # 'None' ensures no error if var doesn't exist. Doing it this way saves
        # a lookup to see if it's in the environment.
        env_vars[var] = os.environ.pop(var, None) # set env_vars[var] equal to the env var.

def restore_env_vars():
    for var in env_vars.iterkeys():
        if env_vars[var]:
           os.environ[var] = env_vars[var]

print "set A,B to none, none"
env_vars = {
    'A': None,
    'B': None
}

print "set environment variables $A,$B to xx, yy"
os.environ['A'] = 'xx'
os.environ['B'] = 'yy'

print_vars_ab()
# A = None
# B = None
# $A = xx
# $B = yy

print "\nclear A,B"
clear_env_vars()

print_vars_ab()
# A = xx
# B = yy
# $A =
# $B =

print "\nrestore A,B"
restore_env_vars()

print_vars_ab()
# A = xx
# B = yy
# $A = xx
# $B = yy
