# import the module for random
import random

my_words = ['pyhthon', 'monty', 'black', 'knight']

# open a file to write to. w = write
f = open('words.txt', 'a')

for number in range(4):
  word = random.choice(my_words)
  f.write(word + '\n')

# close the
f.close()

print 'Done'
