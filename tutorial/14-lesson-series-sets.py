#!/usr/bin/python3


#the following lesson showing some properties of sets


#set always contain unique member
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #the output doesn't contain the doubled items

#fast test for member
print('orange' in basket)
print('strawberry' in basket)

#here is a some properties on sets and set() method demonstration
a = set('limitless')
b = set('limitly')

#unique letters in a
print(a)

#letters in a but not in b
print(a-b)

#letters in b but not in a
print(b-a)

#unique letters in both a and b
print(a|b)

#unique letters common for a and b
print(a&b)

#unique letters not common for a and b
print(a^b)

#sets have also comprehensions  
compset = {x for x in 'abracadabra' if x not in 'abc'}
print(compset)
