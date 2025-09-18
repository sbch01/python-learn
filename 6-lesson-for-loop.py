#!/usr/bin/python3

#Examples of for loop
#You will see that for loop in python is a lot more diffrent then C.
#==============================================

#First example print members of array
#==============================================
words = ['cat', 'window', 'defenestrate']

for w in words:

	print(w, len(w))

#loop all list  and if length of some member is larger then 6 insert once more in the beginig of the list
#===============================================
for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

print(words)

#Range example in for loop
#===============================================

for i in range(1,5):
	print (i)
