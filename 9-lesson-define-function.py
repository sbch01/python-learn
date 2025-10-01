#!/usr/bin/python3

#defining function
#this is fibonaci series  example for custom for variable lenght

def fib (n):

	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print() 

#call the function
fib(200)
