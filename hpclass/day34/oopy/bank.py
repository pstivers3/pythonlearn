'''
Created on Apr 2, 2012

@author: ijessop
'''
import os
import sys

accountData = {}
dataFileName = 'bankData.txt'
baseDataPath = ''

def loadData(bp, dfn):
    """ function to load the data from a text file """
    dataLoaded = False
    dd = {}
    if bp == '':
        bp = os.getcwd()
    while dataLoaded is False:
        fullDataPath = os.path.join(bp , dfn)
        print "current data path = %s" % fullDataPath
        if os.path.exists(fullDataPath):
            print 'Loading account data'
            fp = open(fullDataPath,'r')
            for line in fp.readlines():
                print line
                if line.find('AccountNumber:') == 0:
                    key = line.split(':')[1].strip()
                    dd[key] = {'name':'', 'acctNumber':key, 'balance':0, 'transactions':[]}
                elif line.find('name:') == 0 :
                    dd[key]['name'] = line.split(':')[1].strip()
                elif line.find('balance:') == 0 :
                    dd[key]['balance'] = float(line.split(':')[1].strip())
                elif line.find('trans:') == 0 :
                    dd[key]['transactions'].append(float(line.split(':')[1].strip()))
            dataLoaded = True
        else:
            print 'Data file %s not found ' % fullDataPath
            print ""
            print "Enter Exit to quit"
            print "Enter New to create a new data file in %s" % bp
            ans = raw_input("Enter a new base path to try again %s" % (os.linesep))
            
            if ans.lower() == 'exit':
                sys.exit(0)
            elif ans.lower() == 'new':
                fp = open(fullDataPath,'w')
                fp.close()
            else:
                bp = ans
            #dataLoaded = True
             
    return fullDataPath, dd

def listAccounts(acd):
    """ print a list of account number and name request an account number to select """
    print os.linesep * 25
    for key in acd.keys():
        print "account # %s Name %s" % (key,acd[key]['name'])
        
    validAccount = False
    while validAccount is False:
        ans = raw_input("Enter the account number to select or Exit to return to Menu" )
        if "exit" == ans.lower():
            return None 
        elif ans in acd.keys():
            return ans
        else:
            print "%s is not a valid account  number" % ans

def createAccount(accountNumbers):
    """ create a new account make sure the account number is unique """
    accountOK = False
    print os.linesep * 25
    while accountOK is False:
        ans = raw_input("Enter an account number or Exit to return to Menu" )
        if "exit" == ans.lower():
            return None,{} 
        if ans not in accountNumbers:
            newActNumber = ans
            accountOK = True
            name = raw_input("Enter the Account Name" )
            balOK = False
            while balOK is False:
                bal =  raw_input("Enter the Starting Account balance" )
                try:
                    bal = float(bal)
                    balOK = True
                except ValueError:
                    print "%s is not a valid starting balance it must be a number" % bal
                    
            return newActNumber, {'name':name, 'acctNumber':newActNumber, 'balance':bal, 'transactions':[bal]}
            
        else:
            print "account number %s is already in use" % ans

def debitAccount(act,actData):
    print os.linesep * 25
    print "Enter Debit amount for account %s" % act
    valOK = False
    while valOK is False:
        val =  raw_input("" )
        try:
            val = float(val)
            valOK = True
            if val > 0:
                val = val * -1
            actData[act]['transactions'].append(val)
            actData[act]['balance'] += val
            return actData
        except ValueError:
            print "%s is not a valid debit it must be a number" % val

def creditAccount(act,actData):
    print os.linesep * 25
    print "Enter Credit amount for account %s" % act
    valOK = False
    while valOK is False:
        val =  raw_input("" )
        try:
            val = float(val)
            valOK = True
            if val < 0:
                val = val * -1
            actData[act]['transactions'].append(val)
            actData[act]['balance'] += val
            return actData
        except ValueError:
            print "%s is not a valid credit it must be a number" % val

def accountHistory(act,actData):
    print os.linesep * 25
    for trans in actData[act]['transactions']:
        if trans > 0 :
            print "Credit %.2f" % trans
        else:
            print "Debit %.2f" % trans
    print "balance %.2f" % actData[act]['balance']    
    raw_input("Enter to return to menu" )
    
def saveData(actData, dp):
    """ save the data to a file """
    fp = open(dp,'w')
    
    for key in actData.keys():
        fp.write('AccountNumber:%s%s' % (key, os.linesep))
        fp.write('name:%s%s' % (actData[key]['name'], os.linesep))
        fp.write('balance:%s%s' % (actData[key]['balance'], os.linesep))
        print "transaction list = ", actData[key]['transactions']
        for trans in actData[key]['transactions']:
            fp.write('trans:%s%s' % (trans, os.linesep))
        

def mainMenu(accountData, DataPath):
        
    ans = ''
    currentAccountNumber = None
    while "exit" != ans:
        print os.linesep * 25
        if currentAccountNumber is not None:
            print "------- Currently Selected account %s %s -------" % (currentAccountNumber, accountData[currentAccountNumber]['name'] )
        else:
            print "------- Currently Selected account None -------" 
        print "----------- Menu -------------"
        print "Exit to quit"
        print "Save to save data "
        print "New to create a new account "
        print "List to list accounts"
        
        if currentAccountNumber is not None:
            
            print "Debit current account"
            print "Credit current account"
            print "History of current account"
            
        ans = raw_input("Enter a command " ).lower()
        
        if ans == 'new':
            # create a new account
            (acctnum, accountDict) = createAccount(accountData.keys())
            if acctnum is not None:
                accountData[acctnum] = accountDict 
                print "new account created"
            ans = ''
        elif ans == 'save':
            #save the data file
            saveData(accountData, DataPath)
        elif ans == 'list':
            #list out the accounts
            currentAccountNumber = listAccounts(accountData)
            print "currently selected account = %s" % currentAccountNumber
        elif ans == 'debit':
            # debit the account
            accountData = debitAccount(currentAccountNumber, accountData)
        elif ans == 'credit':
            # credit the account
            accountData = creditAccount(currentAccountNumber, accountData)
        elif ans == 'history':
            accountHistory(currentAccountNumber, accountData)
            
    
    print "goodby"
    
# if we don't have any account data attempt to load it
if len(accountData.keys()) < 1:
    (DataPath, accountData) = loadData(baseDataPath, dataFileName)
    
mainMenu(accountData,DataPath)
