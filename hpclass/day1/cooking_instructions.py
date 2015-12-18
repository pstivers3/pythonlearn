# Data
oven_type = "microwave"
sun = 1.2

# Process
if oven_type == 'microwave':
  print 'heat for 5 minutes'
elif oven_type == 'oven':
  print 'Pre-heat over to 350'
  print 'Bake for 22 minutes'
else:
  if sun > 5.0:
    print 'Leave in direct sun for 5.0 hours'
  else:
    print 'Good Luck!'

