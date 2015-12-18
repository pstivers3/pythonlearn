#!/usr/local/bin/python 

def print_matches(matchtext):
    print "looking for", matchtext
    while True:
	line = (yield)  # get a line of text
	if matchtext in line:
	    print line

matcher = print_matches("python")
matcher.next()
matcher.send("Hellow World")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close()

