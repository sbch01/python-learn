#!/usr/bin/python3

#here is some example for looping  dictionaries


#the follow example show how to loop dictionaries with items() method
#=====================================================================
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(knights.keys())
for i,v in knights.items():
	print(i,v)

#loop through sequence with enumerate
#=====================================================================
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i,v) #print index and value

#looping trough two sequence
#=====================================================================
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

#looping and sorting at a same time with sort()
#=====================================================================
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
	print(i)

#filtering some data in a list
#=====================================================================
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8] #here is a list with float NaN
filtered_data = [] #create a empty list for filtered data
for value in raw_data:
	if not math.isnan(value): #test is NaN
		filtered_data.append(value)

print(filtered_data)
