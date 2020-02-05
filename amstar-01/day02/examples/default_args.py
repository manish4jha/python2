# Function definition 
def printinfo( name = 'Jill', age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", int(age))
   

# Call printinfo function
printinfo( "Tom", 50 ) # Positional mapping
printinfo( "Jerry" )
printinfo( )
printinfo(  name="Donald" ) # Key-word mapping, named mapping
