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
    print(f"My name is {name}")
    print("my name is", name)
