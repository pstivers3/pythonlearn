#!/usr/bin/env python3

f = open("../files/colors.txt")

count = 0 
colors = []

for line in f:
    line = line.strip()  
    colors.append(line)
    if line[0] == "B":
        count +=1

f.close()
print(colors)
print("The number of colors that start with a \"B\" is: " + str(count))
