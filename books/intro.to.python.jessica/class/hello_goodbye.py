# classes inherit from a base object
class Greeter(object):
    # always make self the first argument to a fucntion in a class.
    # has to do with having a pointer back to the class
    # self is the implicit first argument to a function in a class
    
    # define initialization of the class, aka constructor 
    def __init__(self, name):
        # self.<var name> allows you to use the variable in other functions in the class
        self.name = name
    
    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Goodbye " + self.name)

g = Greeter("Jessical")
g.hello()
g.goodbye()

g2 = Greeter("Paul")
g2.hello()
g2.goodbye()

