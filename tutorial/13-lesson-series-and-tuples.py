#!/usr/bin/python3


#the follow lesson will show the some tuples properties

#my_tuple now just hold the string
my_tuple = 'atanas'
print(my_tuple) #actualy is not tuple yet 

#here if we end with comma is convert to tuple, is usless to use tuple for one item just for example
my_tuple = 'atanas',
print(my_tuple) #now is tuple, because of comma

#now lets add more reload with more items
my_tuple = 'orion', 'greek', 'italy'
my_tuple_next = 'apple', 'pear', 'strawbery'

#addig is posible
mearege = my_tuple + my_tuple_next
print(mearege)

#substraction is not posible its pick interpreter error uncomment to see the two row below
#newresult = mearege - my_tuple
#print(newresult)

print(len(my_tuple))
print(len(mearege))

#let's create empty tuple
empty = ()
print(len(empty))

#is intresting property is unpacking of tuple
x,y,z = my_tuple
print(x) #here you have strng now
print(y)
print(z)

#is not posible to assign new value on member it pick error
my_tuple[1] = 'hello'
