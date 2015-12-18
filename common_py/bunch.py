#!/usr/bin/env python2.7

class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
    def display(self):
        print "module name:", self.module_name
        print "tree:", "%r" %  self.tree
        print "one_line:", "%r" %  self.one_line

options=Bunch(module_name='shell',tree=False,one_line=True)

print "options.module_name:", options.module_name

options.display()
