#!/usr/local/bin/python 

import time

# tail a file, similar to tail -f
def tail(f):
    f.seek(0,2)  # move to EOF
    while True:
        line = f.readline()  # try reading a new line of text
	if not line:         # if nothing, sleep breifly and try again
            time.sleep(0.1)
            continue
	yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

tailfile = tail(open("logfile"))
print tailfile
pylines = grep(tailfile,"pyton")
for line in pylines:
    print line, 

