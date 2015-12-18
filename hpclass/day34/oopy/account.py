'''
Created on Apr 4, 2012

@author: ijessop
'''


class account(object):
    '''
    a class for representing a bank account
    '''


    def __init__(self, acctNumber, acctName, acctBal , tlist = None):
        '''
        Constructor
        '''
        self.__acctNum = acctNumber
        self.__acctName = acctName
        self.__acctBal = acctBal
        self.__transactions = []
        
        if tlist is not None:
            self.__transactions.extend(tlist)
        else:
            self.__transactions.append(acctBal)
        
    def __getFloat(self, displayString):
        """
            Ask the user to enter an ammount
            make sure it can be cast to a float
            return the value
        """
        print "Enter %s amount (0) to cancel" % displayString
        valOK = False
        while valOK is False:
            val =  raw_input("" )
            try:
                val = float(val)
                valOK = True
            except ValueError:
                print "%s is not a valid %s it must be a number" % (val, displayString)
                
        return val
        
    def history(self):
        """
        list the transaction history
        """
        for trans in self.__transactions:
            if trans > 0 :
                print "Credit %.2f" % trans
            else:
                print "Debit %.2f" % trans
        print "balance %.2f" % self.balance()
        raw_input("Enter to return to menu")
        
    def debit(self):
        """ debit the account """
        val = self.__getFloat('Debit')
        if val == 0: return
        if val > 0:
            val = val * -1
        self.__transactions.append(val)   
        self.__acctBal += val
        
    def credit(self):
        """ credit account """
        val = self.__getFloat('Credit')
        if val == 0: return
        if val < 0:
            val = val * -1
        self.__transactions.append(val)   
        self.__acctBal += val

    def balance(self):
        """ return the account name """
        return self.__acctBal
    
    def name(self):
        """ retutn the account name """
        return self.__acctName 
    def transactionList(self):
        """ return the list of transactions """
        return self.__transactions
    def accountNumber(self):
        """ return the account number """
        return self.__acctNum
        
if __name__ == '__main__':
    
    myacct = account('1040',"Bob's Cash", 10944.01, [10000,1000,-20.34, -50, -450, 500, -35.65])
    myacct.history()
    myacct.credit()
    myacct.debit()
    myacct.history()
    print "%s" % "\n" * 3
    print "----- summary -----"
    print "account Number %s " % myacct.accountNumber()
    print "account name %s " % myacct.name()
    print "Number of transactions %s " % len(myacct.transactionList())
    print "account balance %s " % myacct.balance()
    

   

        
        
