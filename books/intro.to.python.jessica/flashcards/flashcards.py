# flashcards.py <flash card file>

# sys is a module. It lets us access command line argumments, which are
# stored in sys.argv.

import sys
import random

# if number of command line arguments is less than 2
if len(sys.argv) < 2:
    print("Please supply a flash card file.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

# dictionary (hash)
question_dict = {}

# lines are in format: question, answer
for line in f:
    # strip grabs a line from the file
    # split, splits the line into a list (array)
    entry = line.strip().split(";")
    question = entry[0]
    # strip white space
    answer = entry[1].strip()
    question_dict[question] = answer

f.close

print("Welcome to the flashcard quizzer.")
print("At any time, tye 'quit' to quit.")
print("")

# get a list of all the keys in the dictionary
questions = list(question_dict.keys())

while True:
    question = random.choice(questions)
    answer = question_dict[question]

    print("Question: " + question)
    user_input = input("Your guess: ").strip().lower()
    if user_input == "quit":
        print("Thanks for playing! Goodbye.")
        break
    elif user_input == answer:
        print("Correct!")
    else:
        print("Sorry, the anser was: " + answer)

