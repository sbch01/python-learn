#!/usr/bin/python3

#Here is some while loop example 

#Plot Fibonachi series
#=============================================================
a,b = 0, 1

while a < 10:
	print (a)
	a, b = b, a + b
 
#Insert thre new line 
#=============================================================

for i in range(1,3): #more for loops in next lesson!
	print()



#Plot Fibonachi series on a single line tehnic
#=============================================================
a,b = 0, 1

while a < 1000:
	print (a, end=" ") #end operator used not to transfer output to new line
	a, b = b, a + b 
print()
