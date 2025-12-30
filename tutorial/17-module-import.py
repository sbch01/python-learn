#!/usr/bin/python3


#import functions defined in fibo.py as object mylib
import fibo as mylib

#run the Fibonacci function
mylib.fib(50)

#print the documentation of the function
print(mylib.__doc__)

#print the file and the path to it 
print(mylib.__file__)

#print the name of the file
print(mylib.__name__)

#call help for fibo library you need to press q for exit from it
print(help(mylib))

