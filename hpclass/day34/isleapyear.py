def isLeapYear(year):
# return True if year is divisible by four.

  if year % 4 == 0:
    return True
  if year % 400 == 0:
    if year % 100 == 0:
      return false
  return True 

print 12, isLeapYear(12)
print 100, isLeapYear(100)
print 400, isLeapYear(100)
print 13, isLeapYear(100)

