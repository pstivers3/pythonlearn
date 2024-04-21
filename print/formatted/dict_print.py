#!/usr/bin/env python3

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

reply = '''
Hello %(name)s!
Your age is %(age)s
'''

values = {'name': 'Bob', 'age': 40}
print(reply % values)

