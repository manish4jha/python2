# Python program to demonstrate 
# instance attributes. 
class emp:

    '''
        This is a test class

    '''

    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000
  
    def show(self): 
        print (self.name)
        print (self.salary) 
  
e1 = emp() 
print ("Dictionary form :", vars(e1))
print (dir(e1))
