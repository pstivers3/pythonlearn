#!/usr/bin/env python3

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # return also breaks out of a loop
        except ValueError:
            # pass # catches error but silently. If use pass then comment out print
            print("x is not an integer")

main()
