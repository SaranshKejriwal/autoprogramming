import fileinput
from random import randint #for random threshold of filter 
from functions import *

'''This script uses autowriting to modify the function calls and avoid the loop needed to find the optimum value
run python findvalue.py in terminal'''
opt=26
guess=0
guess=findOptimum(opt)

'''Once the optimum value has been found, the next run of this code would have O(1) complexity, since the function with the loop is no longer called'''
if(guess==opt):
	print "Guess is optimum"

















































