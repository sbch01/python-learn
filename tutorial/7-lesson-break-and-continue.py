#!/usr/bin/python3

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break #when reach break else clause of for loop is not executed
	else:#here is a strange in python that else is part of for loop not part of if statement
		# loop fell through without finding a factor
		print(n, 'is a prime number')

#There is more examples for exceptions in future of this tutorial

for i in range (2,10):
	if i % 2 == 0:
		print ('found even number', i)
		continue
	print ('found a number', i)
