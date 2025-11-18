#!/usr/bin/python3

#Examples of for loop
#You will see that for loop in python is a lot more different then C.
#==============================================

#First example print members of array
#==============================================
words = ['cat', 'window', 'defenestrate']

for w in words:

	print(w, len(w))
print()

#loop all list  and if length of some member is larger then 6 insert once more in the beginning of the list
#===============================================
for w in words[:]:

	if len(w) > 6:
		words.insert(0, w)

print(words)
print("\n")

#Range example in for loop
#===============================================

for i in range(1,5):

	print (i, end=" ")
print("\n")

#Here is little bit different
for i in range(5):

	print(i, end=" ")
print("\n")

#Here is example that loop in range 2 to 10 with step 2
for i in range(2,10,2): #(from, to, step)

	print(i, end=" ")
print("\n")

#Once more with negative numbers
for i in range(-2,-10,-2): #(from, to, step)

	print(i, end=" ")
print("\n")

#Once more combination with range and len
#================================================
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):

	print (i, a[i])

