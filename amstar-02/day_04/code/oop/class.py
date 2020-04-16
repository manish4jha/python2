class student(object):

    nstudents = 0

    # Data/attributes
    def __init__(self, name, cls, rid):
        print('Initializing....')
        self.initialize(name, cls, rid)


    def initialize(self, name, cls, rid):
        self.name = name
        self.cls = cls
        self.regid = rid
        self.physics = 0
        self.maths = 0
        self.chemistry = 0
        self.biology = 0
        self.average = 0
        student.nstudents += 1


    # Functions

    def printinfo(self):
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)
        print('----------------------------------- \n')

    def setMaths(self, marks):
        self.maths = marks

    def setPhysics(self, marks):
        self.physics = marks

    def setChemistry(self, marks):
        self.chemistry = marks

    def setBiology(self, marks):
        self.biology = marks

    def calcAverage(self):
        self.average = (self.physics + self.chemistry + self. biology + self.maths)/4

    def getAverage(self):
        return self.average

#######################################################################################
s1 = student('Rohit', 12, 'A001')
s2 = student('Rohit', 12, 'A001')
s3 = student('Rohit', 12, 'A001')

s1.printinfo()

'''
s1 = student('Rohit', 12, 'A001')
#s1.printinfo()


s1.setPhysics(78)
s1.setMaths(99)
s1.setChemistry(98)
s1.setBiology(97)
#s1.printinfo()



s1.calcAverage()
s1.printinfo()




s2 = student('Aproop', 12, 'A002')
#s1.printinfo()

s2.setPhysics(100)
s2.setMaths(95)
s2.setChemistry(98)
s2.setBiology(99)
#s1.printinfo()

s2.calcAverage()
s2.printinfo()



print(s1.nstudents, s2.nstudents, student.nstudents)
'''
