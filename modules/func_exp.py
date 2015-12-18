#!/usr/bin/env python2.7

def say_hi(first, last='Shmoe'):
    """Documentation: Say Hi.""" 
    print ('\nHi {} {}!'.format(first, last))

def return_test():
    return '\nreturn before printing other text'
    print 'you should not see this'

def main():
    say_hi('Joe')
    print return_test(), '\n'

if __name__=='__main__':
    main()
