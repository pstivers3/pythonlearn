#!/usr/bin/env python3

template = '{0}, {1} and {2}'
print(template.format('Paul', 'David', 'Sue'))

template = '{}, {} and {}'
print(template.format('Paul', 'David', 'Sue'))

template = '{name1}, {name2} and {name3}'
print(template.format(name2 = 'David', name1 = 'Paul', name3 = 'Sue'))

template = '{1}, {0} and {name3}'
print(template.format('David', 'Paul', name3 = 'Sue'))

template = '%s, %s and %s'
print(template % ('Paul', 'David', 'Sue'))

template = '%(name1)s, %(name2)s and %(name3)s'
print(template % dict(name1 = 'Paul', name2 = 'David', name3 = 'Sue'))
