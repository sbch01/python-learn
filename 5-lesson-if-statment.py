#!/usr/bin/python3

#Here is example of if statment

#Input a number
x = int(input("Please enter an integer: "))

#Check number value and print output
#============================================================

if x < 0:
	x = 0 
	print("x is negative and has changed to zero")

elif x == 0:
	print("zero")

elif x == 1:
	print("one")

else:
	print("more")
