#!/usr/bin/env python3

# for illustration. 
# not the best way to do it.
# see 2_...py

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name  = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()

