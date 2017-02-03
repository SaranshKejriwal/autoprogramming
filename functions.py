import fileinput
from random import randint #for random threshold of filter
import sys#to stop execution if needed 
import os

glob_var1=9
flag=0

def editMe():
	glob_var1=10#init
	with open("edit.py", "r+") as f:
		olddata = f.read() # read everything in the file
		f.seek(0)
		newdata = olddata.replace("editMe()","")#avoid infinite loop
		newdata = olddata.replace(str(glob_var1),str(glob_var1+1))
		glob_var1=glob_var1+1
		f.write(newdata)
		f.close()
		#os.exec*()
		os.system("sh runner.sh")
		sys.exit(1)


