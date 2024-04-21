#!/usr/bin/env python3

# Test
# $ ./4_student.py 
#  Name: Paul
# House: Ravenclaw
# Paul from Ravenclaw

class Student:
    def __init__(self, name, house):
        self.name     = name
        self.house    = house

    def __str__(self):   # required in order to print strings from the Student object
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name     = input("Name: ")
    house    = input("House: ")
    return Student(name, house) # constructor

if __name__ == "__main__":
    main()

