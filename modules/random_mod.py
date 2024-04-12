#!/usr/bin/env python3

import random

coin_flip = random.choice(["heads", "tails"])
print("coin flip is", coin_flip)

number = random.randint(1,10)
print("random number from 1 to 10 is", number)

print()
cards = ['jack', 'king', 'queen']
random.shuffle(cards) # will shuffle the list in place
for card in cards:
    print(card)
