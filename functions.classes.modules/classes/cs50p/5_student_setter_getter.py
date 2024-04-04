#!/usr/bin/env python3

# Test
# $ ./4_student.py 
#  Name: Paul
# House: Ravenclaw
# Paul from Ravenclaw

class Student:
    def __init__(self, name, house):
        self.name     = name
        self.house    = house  # will call setter method. If used _house, would circumvent error checking in setter

    def __str__(self):   # required in order to print strings from the Student object
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name=name

    @property # getter
    def house(self):
        return self._house # must match instance variable name in setter

    # any call to .house will go though this function to set house
    @house.setter 
    def house(self, house):  # needs to be same method name as getter
        # error checking is moved into setter method 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") 
        # instance variable name "_house" must be different that instance variable name "house" __init__.
        # By convension use _
        self._house = house

def main():
    student = get_student()
    # This will be prevented by setter method in class Student.
    # student.house = "Number Four, Privet Drive" # overwrite house from get_student method, in student object

    # This overwrite though will still work. Honor system to not use _<name> except in getter and setter
    # student._house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name     = input("Name: ")
    house    = input("House: ")
    return Student(name, house) # constructor

if __name__ == "__main__":
    main()

