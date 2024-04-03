#!/usr/bin/env python3

#!/usr/bin/env python3

class paulclass():
    # Paul's simple class
    def __init__(self, name):
        self.name = name
    def hi(self):
        print("saying %s" % self.name)

pc = paulclass('boo')
pc.hi()

class paulclass2(paulclass):  # inherit from paulclass
    def __init__(self, name, food):  # override init
        paulclass.__init__(self, name) # need to call __init__ from paulclass or self.name will not be known to paulclass2
        self.food = food
    def feedme(self): # add another method
        print("My name is %s. Please feed me %s" % (self.name, self.food))
    def hi(self):  # override hi method from base class
        print("Hi my name is %s. I like %s." % (self.name, self.food))

pc2 = paulclass2('Paul','Pizza')
pc2.feedme()
pc.hi()

