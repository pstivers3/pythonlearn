#!/usr/bin/env python3

number=input("What is the integer? ")

match int(number):
    case 0 | 1 | 2 | 3:
        print("the integer lies between 0 and 3")
    case n if n >= 4:
        print("the integer is greater than or equal to 4")
    case _:
        print("the integer is negative")
