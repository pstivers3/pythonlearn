import random

class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Deck(object):
    def shuffle(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds" ]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit) 
        # randomize the elements of the self.cards list 
        # shuffle (function) of random module takes a list as an argument
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

