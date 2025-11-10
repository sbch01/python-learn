#!/usr/bin/python3

#Here is more about lists as a object 
#list comprehension is about automation creat list of some series in a ratianoal way

#this creat list of numbers  square of two 
#--------------------------------------------
squares = [x**2 for x in range(10)]
print(squares)

#The follow example do the same thing but with more command line
#so is more rational to use statment above 
#squares = []
#	 for x in range(10):
#		squares.append(x**2)


#combine list of tuples with condition to not be equal
#--------------------------------------------
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

#here is a example for manipulation of lists in comprehenst way!
#--------------------------------------------
vec = [-3, -1, 1, 4, 6]
print(vec)
print([x*2 for x in vec]) #here is double the numbers in vec
print([abs(x) for x in vec]) #here make all numbers positive
print([(x, x**2) for x in range(6)]) #create list of tuples

#let creat the matrix
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
#and now lets transpose this matrix
trans = [[row[i] for row in matrix] for i in range(4)] 
print(trans)

#del statment examples
#--------------------------------------------
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:] #also can be used del a without [:]
print(a)
