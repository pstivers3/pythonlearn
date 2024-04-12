#!/usr/bin/env python3

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# need this if this is a module to be called by another file
# otherwise main will be called by the import  from the other file
if __name__ == "__main__":
    main()
