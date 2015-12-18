# Import random Module
import random

# Create an empty list to hold the words.
words = list()

# Read words from file into a list. Remove the new line character.
f = open('words.txt', 'r')
for line in f:
    word = line.strip('\n')
    words.append(word)
f.close()

# Use random.choice(words) to pick a word.
the_word = random.choice(words)

# Move the chosen word into a list of letters with list(the_word)
the_word_letters = list(the_word)

# Copy the word, then sort in place using the .sort() method
copy_the_word_letters = the_word_letters
copy_the_word_letters.sort()

# Itterate over the sorted letters to print to screen
for letter in  copy_the_word_letters:
    print letter

# Make a blank guess, like guess = ''
guess = ''

# Use a while loop to keep asking for a guess, untill it is correct
guess_number = 1
while (guess != the_word):
    print "Enter guess %d" % guess_number
    guess = raw_input()
    if (guess == the_word):
        print "Congratulations!"
    else:
        print "Please try again"

    guess_number = guess_number + 1

print 'Press enter to exit'    
raw_input()

