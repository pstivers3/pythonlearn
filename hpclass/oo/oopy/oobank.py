'''
Created on Apr 2, 2012

@author: ijessop
'''
import os
import sys
import account

accountList = {}
dataFileName = 'bankData.txt'
baseDataPath = ''

def loadData(bp, dfn):
    """ function to load the data from a text file """
    dataLoaded = False
    if bp == '':
        bp = os.getcwd()
    while dataLoaded is False:
        fullDataPath = os.path.join(bp , dfn)
        print "current data path = %s" % fullDataPath
        if os.path.exists(fullDataPath):
            print 'Loading account data'
            fp = open(fullDataPath,'r')
            acctNum = None
            acctName = None
            acctBal = None
            tlist = []
            for line in fp.readlines():
                print line
                if line.find('AccountNumber:') == 0:
                    if acctNum is not None:
                        #Instantiate a new account object and add it to the account list
                        accountList[acctNum] = account.account(acctNum, acctName, acctBal, tlist)
                        tlist=[]
                    acctNum = line.split(':')[1].strip()
                elif line.find('name:') == 0 :
                    acctName = line.split(':')[1].strip()
                elif line.find('balance:') == 0 :
                    acctBal = float(line.split(':')[1].strip())
                elif line.find('trans:') == 0 :
                    tlist.append(float(line.split(':')[1].strip()))
            # load the last account
            accountList[acctNum] = account.account(acctNum, acctName, acctBal, tlist)
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
             
    return fullDataPath, accountList

def listAccounts(acd):
    """ print a list of account number and name request an account number to select """
    print os.linesep * 25
    for key in acd.keys():
        print "account # %s Name %s" % (key,acd[key].name())
        
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
            return None 
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
            #Instantiate a new account object and add it to the account list        
            return account.account(newActNumber, name, bal)
            
        else:
            print "account number %s is already in use" % ans

def saveData(actData, dp):
    """ save the data to a file """
    fp = open(dp,'w')
    
    for key in actData.keys():
        fp.write('AccountNumber:%s%s' % (key , os.linesep))
        fp.write('name:%s%s' % (actData[key].name(), os.linesep))
        fp.write('balance:%s%s' % (actData[key].balance(), os.linesep))
        for trans in actData[key].transactionList():
            fp.write('trans:%s%s' % (trans, os.linesep))
        

def mainMenu(accountLata, DataPath):
        
    ans = ''
    currentAccountNumber = None
    while "exit" != ans:
        print os.linesep * 25
        if currentAccountNumber is not None:
            print "------- Currently Selected account %s %s -------" % (currentAccountNumber, accountList[currentAccountNumber].name() )
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
            acct = createAccount(accountList.keys())
            if acct is not None:
                accountList[acct.accountNumber()] = acct 
                print "new account created"
            ans = ''
        elif ans == 'save':
            #save the data file
            saveData(accountList, DataPath)
        elif ans == 'list':
            #list out the accounts
            currentAccountNumber = listAccounts(accountList)
            print "currently selected account = %s" % currentAccountNumber
        elif ans == 'debit':
            # debit the account
            accountList[currentAccountNumber].debit()
        elif ans == 'credit':
            # credit the account
            accountList[currentAccountNumber].credit()
        elif ans == 'history':
            accountList[currentAccountNumber].history()
            
    
    print "goodby"
    
# if we don't have any account data attempt to load it
if len(accountList.keys()) < 1:
    (DataPath, accountData) = loadData(baseDataPath, dataFileName)
    print accountList
    
mainMenu(accountData,DataPath)
