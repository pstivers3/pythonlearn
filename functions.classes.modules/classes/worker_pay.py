#!/usr/bin/env python3

class Worker:
    def __init__(self, name, pay):    # initialize when created
        self.name = name              # self is the new object
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1] # split string on blanks
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)   # update pay in place

bob = Worker('Bob Smith', 50000)      # make two instances
sue = Worker('Sue Jones', 60000)      

print('Bob\'s last name: ', bob.lastName())

sue.giveRaise(.10)
print('Sue\'s new pay: ', sue.pay)

