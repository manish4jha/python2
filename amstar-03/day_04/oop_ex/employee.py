class employee(object):

    # Data/attribute

    def __init__(self, n, a, c, s):
        self.name = n
        self.age  = a
        self.company = c
        self.salary = s

    '''
    def __init__(self):
        self.name = ''
        self.age  = ''
        self.company = ''
        self.salary = ''
    '''
    # Methods/functions

    def printstate(self):
        print('STATE OF OBJECT', self)
        print(self.name, self.age, self.company, self.salary)

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name


    def calctax(self):
        pass



# ------------------------------------------------------------- #


e1 = employee('Vivek', 30, 'Oracle', '400000')
# e1 = employee()
# e1.name = 'Vivek'

# e1.setname('Vivek')
# print('Name in E1 : ', e1.getname())
e1.printstate()



e1.setname('Rajesh')
#print('Name in E1 : ', e1.getname())
e1.printstate()

#e2 = employee('Raj', 32, 'Infosys', '500000')
#e2.printstate()
