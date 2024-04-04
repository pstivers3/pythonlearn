#!/usr/bin/env python3

# dictionary
ages={'Paul': 50,
      'Mary': 36,
      'Jim': 22}

for person in ages:
    print(person, ages[person])

print()

# list of dictionaries
people = [
    {"name": "Paul", "age": 50, "height": 6},
    {"name": "Sue", "age": 52, "height": 5},
    {"name": "Mary", "age": 36, "height": None}
]

for person in people:
    print(person["name"], person['age'], person['height'], sep=", ")

