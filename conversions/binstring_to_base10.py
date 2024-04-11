#!/usr/bin/env python3

b = '11101'
i = 0
print("i =", i)
print("b =", b)

while b != '':
    i = i * 2 + (ord(b[0]) - ord('0'))
    b = b[1:]
    print("i =", i)
    print("b =", b)

print(i)

''' needs work
print("\nSecond Way")
b = '11101'
i = 0

while len(b) != 0:
    val = b[-1] * 2^i
'''

