#!/usr/local/bin/python 

def countdown(n):
    print "Counting down!"
    while n > 0:
	yield n  # generate a value (n)
	n -= 1

c = countdown(5)
for i in range(5):
    print c.next()

for i in countdown(5):
    print i,
	
