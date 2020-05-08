class student(object):

    # Data/Attribute
    def __init__(self, n, a, r):
        self.name = n
        self.age = a
        self.regid = r
        self.marks = {}
        self.avg = 0
        self.rank = 0

        self.initmarks()


    # Associated functions
    def printinfo(self):
        print('NAME: ', self.name)
        print('AGE: ', self.age)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.marks['math'])
        print('PHYSICS  : ', self.marks['phy'])
        print('CHEMISTRY: ', self.marks['chem'])
        print('BIOLOGY  : ', self.marks['bio'])
        print('-----------------------------------')
        print('AVERAGE  : ', self.avg)
        print('RANK     : ', self.rank)
        print('\n\n')

    def initmarks(self):
        for subject in ['phy','chem','math', 'bio']:
            self.marks.setdefault(subject, 0)



    def calcaverage(self):
        self.avg = sum(self.marks.values())/len(self.marks.values())

    # Getters
            
    def getaverage(self):
        self.calcaverage()
        return self.avg

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getregid(self):
        return self.regid

    def getrank(self):
        return self.rank

    def getmarkslist(self):
        return self.marks

    # Setters

    def setrank(self, rank):
        print('Setting rank')
        if(str(rank).isdigit()):
            self.rank = rank

    def setmarks(self, sub, marks):
        if(sub in ['phy','chem','math', 'bio'] and str(marks).isdigit()):
            self.marks[sub] = marks
        else:
            print('Incorrect subject code')



###################################################################################

if __name__ == '__main__':

    s1 = student('Vijay', 14, 'HPE007')
    s1.printinfo()
    s1.setmarks('phy', 100)
    s1.setmarks('chem', 100)
    s1.setmarks('math', '%^')
    s1.setmarks('biology', 100)
    s1.printinfo()
    

    s2 = student('Hemanth', 14, 'HPE006')
    s2.printinfo()

    s1.setmarks('math', 88)
    s1.setmarks('bio', 100)
    s1.printinfo()

    s1avg = s1.getaverage()
    if(s1avg > 50):
        s1.setrank(1)

    s1.printinfo()

    
