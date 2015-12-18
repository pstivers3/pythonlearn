f = open("testfile2", "r")

count = 0 
colors = []

for line in f:
    line = line.strip()  
    colors.append(line)
    if line[0] == "B":
        count +=1

f.close()
print(colors)
print("Then number of colors that start with a \"B\" is: " + str(count))
