#Here is example library 
#If you see missing !/usr/bin/python3 in the beginning
#as well you see a lot of """""" quotes
#this is the way to give good documentation of your library

#the first quote give brief explanation of library as well is contain in mylib.__doc__ var
"""
This is library custom library for Fibonacci series plot
The purpose of library is python practice
"""
__author__ = "S. Banchev"
__version__= "0.1"
__license__= "Public domain"


#function with no return is called procedure
#====================================================================
def fib (n):

	#here is placed quotes for functions and must be placed with one tab
	#the same as function code
	"""
	Procedure fib piloting Fibonacci series

	Parameter:
	----------
	n: the end of series

	"""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print() 


#function with return is called function
#====================================================================
def fib2 (n):


	"""
	Function fib2 return Fibonacci series

	Parameter:
	----------
	n: the end of series

	Return:
	-------
	series: list of series from 0 to n the end of series
	"""

	series=[]
	a,b =0,1
	while a<n:
		series.append(a)
		a,b = b, a+b
	return series


