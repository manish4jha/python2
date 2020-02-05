class student(object):

    # Variables/data points

    def __init__(self, n, a, g):
        self.name    = n
        self.age     = a
        self.gender  = g
        self.marks   = {}
        self.average = 0
        self.rank    = 0


    # Functions/Methods

    # Convenience functions
    def printinfo(self):
        print('NAME   : ', self.name)
        print("AGE    : ", self.age)
        print("GENDER : ", self.gender)
        print("\n")
    
    # Setters

    def setname(self, name):
        self.name = name

    def setage(self, age):
        self.age = age

    def setgender(self, gen):
        self.gender = gen
        
    # Getters

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getgender(self):
        return self.gender
    
    # House keeping functions


###################################################################

if __name__ == '__main__':

    s1 = student('Zach', 14, 'M')
    s2 = student('Jill', 14, 'F')
    s3 = student('Mike', 13, 'M')
    s4 = student('Tom', 12, 'M')

    s1.printinfo()
    s2.printinfo()
    s3.printinfo()
    s4.printinfo()

    print('Pulling details for Jill')
    print(s2.getname())
    print(s2.getage())
    print(s2.getgender())
