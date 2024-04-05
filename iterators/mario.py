#!/usr/bin/env python3

def main():
    print_column(3)
    print()
    p_column(4)
    print()
    print_row(4)
    print()
    print_square(3)
    print()
    print_rectangle(6,2)

def print_column(height):
    for _ in range(height):
        print("  #")

def p_column(height):
    print("  #\n" * height, end='')

def print_row(width):
    print("#" * width)

def print_square(size):
    for i in range(size):
        print("#" * size)

def print_rectangle(width,height):
    for _ in range(height):
        print_row(width)

main()
