word_file = 'words.txt'

# import the module used for random
import random

# Create  an empty list
word_list = list()

# read words from file
f = open(word_file, 'r')
for line in f:
  word = line.strip('\n')
  word_list.append(word)
f.close()

# Use random.choice(words) to pick a word.
word = random.choice(word_list)

# Move the chosen word into a list of letters with list(the_word)
letter_list = list(word)

# Copy the word, then sort in place using the .sort() method
letter_list.sort()

# Iterate over the sorted letters to print to screen
for letter in letter_list:
  print letter

# Use a while loop to keep asking for a guess, until it is correct
guess = ''
while guess != word:
  guess = raw_input('guess the word: ')
  if guess == word:
    print 'right!'
  else: 
    print 'Wrong. Try again.'
  
