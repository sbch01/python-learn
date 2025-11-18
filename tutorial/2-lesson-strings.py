#!/usr/bin/python3

#In this py file we will play with stings

#next few example show the nested quotes rules
#-----------------------------------------------------------
print('spam eggs') # single quotes

print('doesn\'t') 

print("doesn't") 

print('"Yes," they said.') 

print("\"Yes,\" they said.") 

print('"Isn\'t," they said`') 
#-----------------------------------------------------------

#Here is example of new line use in python

#-----------------------------------------------------------
print('C:"\"some\name') # here \n means newline!

print(r'C:\some\name''\n\n\n') # here \n is not printed because there is r (raw) in the front of string!
#-----------------------------------------------------------

#Here is a example of """....""" triple quotes
#-----------------------------------------------------------
print("""\
Usage: thingy [OPTIONS]
		-h		Display this usage message
		-H hostname	Hostname to connect to
""")
#-----------------------------------------------------------

#Here is example how strings behave like numbers add
#-----------------------------------------------------------
print(3 * 'un ' + 'ium\n')

FirstName = 'Stoian'
print(FirstName + ' Banchev\n')
#-----------------------------------------------------------

#Here is example of how you can access a single or multiple charter of string
#-----------------------------------------------------------
String = "Hello World"
print(String,'\n')
print('[0]->',String[0])
print('[3]->,',String[3])
print('[0:2]->',String[0:2])
print('[-1]->',String[-1])
print('[-3]->',String[-3])
print('[2:-2]->',String[2:-2])
print('[:-5]->',String[:-5])
print('[4:]->',String[4:],'\n')
#-----------------------------------------------------------

#The end of the lesson is the length of the string
print("The length of the string 'Hello_world' is:")
print(len('Hello_world'))
