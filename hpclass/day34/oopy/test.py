class account():

    def __init__(self, acctnbr, accountname, bal):
        print "init has run"
        self.acctName = accountname
        self.acctBal = bal
        self.acctNum = acctnbr
        self.acctTrans = []

    def credit(self,amt):
        """ credit the account """
        if amt < 1:
            amt = amt * -1
        self.acctTrans.append(amt)
        self.acctBal = self.acctBal + amt

    def debit (self, amt):
        """ debit the account"""
        if amt > 1:
            amt = amt * -1
        self.acctTrans.append(amt)
        self.acctBal = self.acctBal + amt

    def history(self):
        for tran in self.acctTrans:
            print tran

    def balance(self):
        print self.acctBal

    def details(self):
        print "account number %s account name %s account balance %s " % (self.acctNum, self.acctName, self.acctBal)
    


if __name__ == '__main__':

    
    ma = account(430,'Bobs cash', 2000)
    ma.credit(20)
    ma.debit(40)
    ma.debit(60)
    ma.history()
    ma.balance()
    ma.details()
    
