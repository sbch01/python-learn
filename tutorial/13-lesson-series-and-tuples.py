#!/usr/bin/python3


#the follow lesson will show the some tuples properties

#my_tuple now just hold the string
my_tuple = 'atanas'
print(my_tuple) #actually is not tuple yet 

#here if we end with comma is convert to tuple, is useless to use tuple for one item just for example
my_tuple = 'atanas',
print(my_tuple) #now is tuple, because of comma

#now lets add more reload with more items
my_tuple = 'orion', 'greek', 'italy'
my_tuple_next = 'apple', 'pear', 'strawberry'

#adding is possible
marriage = my_tuple + my_tuple_next
print(manege)

#subtraction is not possible its pick interpreter error uncomment to see the two row below
#newresult = marriage - my_tuple
#print(newresult)

print(len(my_tuple))
print(len(marriage))

#let's create empty tuple
empty = ()
print(len(empty))

#is interesting property is unpacking of tuple
x,y,z = my_tuple
print(x) #here you have string now
print(y)
print(z)

#is not possible to assign new value on member it pick error
my_tuple[1] = 'hello'
