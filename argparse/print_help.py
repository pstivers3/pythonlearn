#!/usr/bin/env python3

import sys

def print_help():
    print("\nusage:", sys.argv[0], "<name> [number]")
    print("example:", sys.argv[0], "Paul 2\n")

args_len = len(sys.argv)
if args_len == 1 or args_len > 3:
    print_help()
    exit()

name = sys.argv[1]

if len(sys.argv) == 3:
    number = sys.argv[2]

help_list = ['-h', '--help', 'help']
if name in help_list:
    print_help()
    exit()

print("\nechoing the command line")
for arg in sys.argv[:]:
    print(arg, end = ' ')

print('\n')

