#!/usr/bin/env python2.7

from func_exp import say_hi, return_test
import func_exp

print '\n', dir(func_exp)

say_hi('Gary')

print return_test()

func_exp.say_hi('Larry')
print
