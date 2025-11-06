#!/usr/bin/python3

#Here is more about lists as a object 
#We gone to play with some methods of list object

#crete two list of names and animals
newlist = ["john","stoian","peter","stoian"]
iterable = ['dog','cat','mouse']

#count item in list
#--------------------------------------------
print(newlist.count('stoian'))

#append on list
#--------------------------------------------
newlist.append("atanas") #add item on the tail of list
print(newlist)

#extend on list
#--------------------------------------------
newlist.extend(iterable) #adding list iterable to the first one newlist
print(newlist)

#isert on list
#--------------------------------------------
newlist.insert(1, 'newname') #add newname member in list after first member in the list
print(newlist)

#remove from list
#--------------------------------------------
newlist.remove('stoian') #search stoian in list and remove the first item with that name
print(newlist)

#pop from list
#--------------------------------------------
lastname = newlist.pop() #remove last item from list and put it to lastname var
firstname = newlist.pop(0) #remove first item from list and put it to firstname var
#print the result
print(lastname)
print(firstname)
print(newlist)

#sort list
#--------------------------------------------
newlist.sort() #here is sorting list in alphabet sequence
print(newlist)

#reverse list
#--------------------------------------------
newlist.reverse()
print(newlist)

#index return list
#--------------------------------------------
print(newlist.index('atanas')) #return index number of stoian item in list

#use list as stack
#--------------------------------------------
st = [2,3,6]
st.append(4)
st.append(8)
print(st.pop())

#use list as queues
#--------------------------------------------
from collections import deque #import some is like include in C it is necessery to use deque (double end queue) 
qu = deque([3,6,8,2]) #create qu object of class deque
print(qu.popleft())
print(qu)
