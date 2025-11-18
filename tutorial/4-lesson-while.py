#!/usr/bin/python3

#Here is some while loop example 

#Plot Fibonacci series
#=============================================================
a,b = 0, 1

while a < 10:
	print (a)
	a, b = b, a + b
 
#Insert three new line 
#=============================================================

for i in range(1,3): #more for loops in next lesson!
	print()



#Plot Fibonacci series on a single line  
#=============================================================
a,b = 0, 1

while a < 1000:
	print (a, end=" ") #end operator used not to transfer output to new line
	a, b = b, a + b 
print()

#Let's play with while loop once more and plot the power of two 
#=============================================================

a = 2
while a < 65:
	print("2^" ,a , "=" , 2**a )
	a = a + 2
