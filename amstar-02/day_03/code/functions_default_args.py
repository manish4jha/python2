# Function definition 
def printinfo(name='Jerry', age=35):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)

def add2(a=10, b=20):
    s = a + b
    return s

printinfo( age=15 )

x = add2(50)
print('X : ', x)
