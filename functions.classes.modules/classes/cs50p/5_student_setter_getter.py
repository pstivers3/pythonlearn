#!/usr/bin/env python3

# Test
# $ ./4_student.py 
#  Name: Paul
# House: Ravenclaw
# Paul from Ravenclaw

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name     = name
        self.house    = house  # will call setter method

    def __str__(self):   # required in order to print strings from the Student object
        return f"{self.name} from {self.house}"

    # Getter - must go through this function to get house
    @property 
    def house(self):
        return self._house # must match method name in setter 

    # Setter - must go through this function to set house
    @house.setter 
    def house(self, house):  # needs to be same method name as getter
        # error checking is moved into setter method 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") 
        self._house = house # must be named differently than method in __init__

def main():
    student = get_student()
    # This will be prevented by setter method in class Student.
    # student.house = "Number Four, Privet Drive" # overwrite house from get_student method, in student object
    print(student)


def get_student():
    name     = input("Name: ")
    house    = input("House: ")
    return Student(name, house) # constructor
        

if __name__ == "__main__":
    main()

