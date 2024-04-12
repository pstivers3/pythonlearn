#!/usr/bin/env python3

print('*' * 5, end='')
print('-' * 5, "\n")

# dictionaries
ages={'Paul': 50,
      'Mary': 36,
      'Jim': 22}

for person in ages:
    print(person, ages[person])

print()

# arrays
names={ 'David',
        'Paul',
        'Judy'
      }

for name in names:
    print("my name is", name)

print()

# formatted
kind="sheep"
print(f"a {kind} dog")
print("a {0} dog".format(kind))
print("a %s dog" % kind)

print('\nThat is %d %s bird!' % (1, 'dead'))
print('That is {0} {1} bird!'.format(1, 'dead'))

# tripple quotes
print('''
go
  tell
it!''')
