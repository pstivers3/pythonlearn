import math

def area(r):
  """
  Returns the area from a given radius
  """
  value = math.pi * r**2.0
  return value

if __name__ == '__main__':
  #Yahoo some one called me directly
  # Test code
  print 'For radius = 1.0'
  print 'Expect : 3.1415...'
  print 'And got:',area(1.0)
   
