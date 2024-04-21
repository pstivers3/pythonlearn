#!/usr/bin/env python3

class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Define custom addition behavior
        return self.value + other

# Create an instance of MyClass
obj1 = MyClass(5)

# Adding 3 to the object using the overloaded + operator
result = obj1 + 3
print("Result of addition:", result)  # Output: Result of addition: 8
