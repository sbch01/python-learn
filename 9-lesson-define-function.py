#!/usr/bin/python3

#defining function
#this is fibonaci series  example for custom for variable lenght

#function with no return is caled prodcedure
#====================================================================
def fib (n):

	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print() 

#call the function
fib(100)

#function with return is caled function
#====================================================================
def fib2 (n):

	series=[]
	a,b =0,1
	while a<n:
		series.append(a)
		a,b = b, a+b
	return series

print(fib2(170))

#here is a example of parameter pass to function here is default parameters
#====================================================================
def ask_ok(prompt, retries=4, reminder='Please try again!'):
	cnt = 0
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'): #here is new key word in
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		cnt = cnt + 1
		if retries == cnt:
			#raise ValueError('invalid user response')
			print('sorry you miss',cnt,' times')
			break
		print(reminder)

#you can call subroutine with one parameter only all others are the basic
ask_ok('Insert your answer:')
#here calling the function with more custom parameters
ask_ok('insert your second try:', 2,'once more try')



#Here is example of passing lists and dictionary to the function
#====================================================================

#First of all lets creat list of names
food_list = ['apple', 'pear', 'strawberry']

#Let's creat a dictioanry
person_info = {'name':'Stoian', 'Age': 40, 'Sex': 'Male'}

#This is a function with three members

def print_list (food1,food2,food3):
	print('food1', food1)
	print('food2', food2)
	print('food3', food3)

#Here we pass the members as list
print_list (*food_list)

#Her is subroutine print personal info dictonary
def print_personal_info (**dic):
	for kw in dic:
		print(kw,':',dic[kw])

#So here pass the personal info as dictionary
print_personal_info(**person_info)
