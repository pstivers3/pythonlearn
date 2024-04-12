#!/usr/bin/env python3

kind="sheep"
# expression 
print("a %s dog" % kind)
print(f"a {kind} dog")
# function 
print("a {0} dog".format(kind))

# expression
print('\nThat is %d %s bird!' % (1, 'dead'))
# function
print('That is {0} {1} bird!'.format(1, 'dead'))
