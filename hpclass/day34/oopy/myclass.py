class myclass(object):

    #class variables
    icount = 0
    ictotal = 0
    
    def __init__(self, name):
        """the init method """
        print "Creating new instance of myclass"
        self.name = name
        self._add()
        self.createorder = myclass.ictotal
        self._privatevar = 'private'
        self.__hiddenvar = 'hidden'

    def _add(self):
        """ add 1 to total count """
        myclass.icount += 1
        myclass.ictotal += 1

    def hi(self):
        print "Hello World my create order is %d of %d " % (self.createorder, myclass.ictotal)

    def howmany(self):
        print myclass.icount

    def when(self):
        print self.createorder

    def who(self):
        print "My name is %s " % self.name

    def rename(self, newname):
        self.name = newname
        
    def __del__(self):
        print "deleting instance of myclass"
        myclass.icount -= 1
if __name__ == '__main__':

    mc = myclass('Bob')
    mc.hi()
    mc.howmany()
    mc.who()
    
    del(mc)
