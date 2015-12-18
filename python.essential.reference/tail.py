#!/usr/local/bin/python 

import time
file = open("logfile") 

# tail a file, similar to tail -f
def tail(f):
    f.seek(0,2)  # move to EOF
    while True:
        line = f.readline()  # try reading a new line of text
	if not line:         # if nothing, sleep breifly and try again
            time.sleep(0.1)
            continue
        print line.lstrip(),

tail(file)
