# import the module for random
import random

my_words = ['python', 'monty', 'black', 'knight']

# open a file to write to. w = write
f = open('words.txt', 'a')

count = 1000
python = 0
monty = 0
black = 0
knight = 0

while(count > 0):
  for number in range(4):
    word = random.choice(my_words)
    if word == 'python':
      python = python + 1
    if word == 'monty':
      monty = monty + 1
    if word == 'black':
      black = black + 1
    if word == 'knight':
      knight = knight + 1

#     f.write(word + '\n')
  count = count - 1

# close the
f.close()

print 'python', python
print 'monty', monty 
print 'black', black 
print 'knight', knight 
