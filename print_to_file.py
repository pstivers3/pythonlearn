f = open('testfile', 'w')
a = 2
b = 1.03
print >>f, "%3d %0.2f" % (a, b)
f.write("%3d %0.2f\n" % (a,b))
f.close()
