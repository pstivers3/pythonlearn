#!/usr/bin/env python3

# Test
# $ ./4_student.py 
#  Name: Paul
# House: Ravenclaw
# Patronus: Stag
# Expecto Patronum!
# Paul from Ravenclaw
# 🐴

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            print("Paul says wrong house!")
            raise ValueError("Invalid house") 
        self.name     = name
        self.house    = house
        self.patronus = patronus

    def __str__(self):   # required in order to print strings from the Student object
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print(student) # can do this because of __str__ method
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name     = input("Name: ")
    house    = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # constructor
        

if __name__ == "__main__":
    main()

