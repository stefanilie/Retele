import math

class Hamming:

	@staticmethod
	def is2pow(num):
		return ((num & (num - 1)) == 0) and num != 0

	
	def readData():
		print "Algoritmul Hamming(7, 4)"
		print "Introduceti cei 4 biti de date: d1, d2, d3, d4"
	
print Hamming.is2pow(4);
print Hamming.is2pow(5);