my_words = ['pyhthon', 'monty', 'black', 'knight']

# open a file to write to. w = write
f = open('words.txt', 'w')

for word in my_words:
  f.write(word + '\n')

# close the file, cause we're done
f.close()

print 'Done'
