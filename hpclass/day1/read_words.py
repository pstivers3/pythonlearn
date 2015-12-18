# create an empty list
my_words = list()

# open a file to read, r = read 
f = open('words.txt', 'r')

# Iterate over the list and read from the file
for line in f:
  word = line.strip('\n')
  my_words.append(word)

# close the file, cause we're done
f.close()

print my_words 
