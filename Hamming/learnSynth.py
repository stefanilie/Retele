mode=input('Baga valouare, mo: ')
val= [mode]
for x in range(0, mode):
    print "We're on time %d: " % (x)
    val[x] = bin(input())
print"dupa citire:"
for x in range(0, mode):
	print "%d: %d" %x % val[x] 