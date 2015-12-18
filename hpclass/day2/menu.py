#!/usr/bin/env python

values = {}

cmd = 'p'
while cmd != 'q':
  if cmd == 'a':
    # Request a name and phone extension 
    print 'Add'
    print 'Enter a name'
    name = raw_input()
    print 'Enter an extension'
    value = raw_input()
    values[name] = value

  elif cmd == 'p':
    # Print out all names in list
    print '\nItems in list'
    for key in values:
      print key,':', values[key] 
    print
 
  else:
    print 'Command not known'

  print 'Menu:'
  print 'a to add'
  print 'p to print'
  print 'q to quit'

  cmd = raw_input()
print
