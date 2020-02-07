# Python program to illustrate 
# *args with first extra argument 
def myFun(arg1, arg2, arg3, arg4, *argv): 
	print ("First argument :", arg1)
	print ("Length of argv :", len(argv))
	for arg in argv: 
		print("Next argument through *argv :", arg) 

myFun('Hello', 'Welcome', 'to', 'python') 
