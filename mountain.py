print "input height :",
height = input()

for i in range(0,height):
	for j in range(0,height-1-i):
		print ' ',
	for j in range(0,2*i+1):
		print '*',
	print ''

