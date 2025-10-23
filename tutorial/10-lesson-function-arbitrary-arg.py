#!/usr/bin/python3

#define function the *args accept tuples of args
def write_multiple_items(f, separator, *args):
	f.write(separator.join(args))

#open file and call function above to write in
#more for file maipulation later in tutorial
with open("file.txt", "w") as myfile:
	write_multiple_items(myfile,"/",'1','2','3','4','5')

#Typical the *args is placed at the end of arguments,
#but is posible to be placed in the beginig, see the following example

def join_str (*args, sep="/"):
	return sep.join(args)

print(join_str('1','2','3'))
#Another call with difrent deparator
print(join_str('1','2','3',sep='.'))
