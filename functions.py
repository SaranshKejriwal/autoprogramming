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

def replaceGuesser(optimum_val):
	with open("findvalue.py", "r+") as f:
		olddata = f.read() # read everything in the file
		f.seek(0)
		newdata = olddata.replace("findOptimum(opt)",str(optimum_val))#avoid infinite loop
		f.write(newdata)
		f.close()
		#os.exec*()
		os.system("sh runner_findVal.sh")
		sys.exit(1)

def findOptimum(glob_optimum):
	val=0
	for val in range(100):
		if(val==glob_optimum):
			replaceGuesser(val)
			break
	return val


