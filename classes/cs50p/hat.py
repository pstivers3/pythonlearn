#!/usr/bin/env python3

import random

class Hat:
   
    # class (cls) variable, not an instance variable
    # no def __init__(self):
    houses = ["blue", "green", "red", "yellow"]
    
    @classmethod 
    def sort(cls, name):
        print(name, "is in a", random.choice(cls.houses), "house")

Hat.sort("Harry")
        
