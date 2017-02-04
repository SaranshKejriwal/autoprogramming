import fileinput
from random import randint #for random threshold of filter 
from functions import *

'''this is the first code that uses autoprog
run using python edit.py'''
with open("edit.py", "r+") as f:
	#olddata = f.read() # read everything in the file
	f.seek(0) # rewind
	print "11"
	editMe()
	#f.close()
	#newdata = olddata.replace("filter_func()","filter_func2()")
	#filter_func2()
	#f = open(fileout,'w')
	#f.write(newdata)
	#f.close()

'''

f.write("new line\n" + old) # write the new line before
f = open(filein,'r')
filedata = f.read()'''





