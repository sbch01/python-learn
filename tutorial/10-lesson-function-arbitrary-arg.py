#!/usr/bin/python3

def write_multiple_items(f, separator, *args):
	f.write(separator.join(str(args)))


with open("file.txt", "w") as myfile:
	write_multiple_items(myfile,"/",1,2,3,4,5)
