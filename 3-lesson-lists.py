#!/usr/bin/python3

#In this py file we will play with lists

#lets creat a list of squares
squares = [1,4,9,16,25,36]

#filtering of list example
#---------------------------------------------------
print(squares [0])
print(squares [-1])
print(squares [:])
#---------------------------------------------------

#concentration of two list
#---------------------------------------------------
squares = squares + [49, 64, 89]
print(squares[:])
#---------------------------------------------------

#append to list example
#---------------------------------------------------
squares.append (100)
squares.append (11 ** 2)
print(squares[:])
#---------------------------------------------------

#remove and replace some member of the list
#---------------------------------------------------
squares[0:2] = []	
squares[-1] = 0	
print(squares[:])
#---------------------------------------------------
