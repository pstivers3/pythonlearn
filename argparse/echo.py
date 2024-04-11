#!/usr/bin/env python3

# usage example: ./echo.py help -a -b
import sys

print(sys.argv[1])
for arg in sys.argv[:]:
    print(arg, end=' ')
print()
