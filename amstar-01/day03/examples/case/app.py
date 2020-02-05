import os
import os.path
os.chdir(r"C:\Users\Purushotham\Desktop\code\case")

import student
objs = []

# LAYER #1

# Open the file and read the first line
# first line represents columns

f = open(r"C:\Users\Purushotham\Desktop\code\case\students.csv", "r")
columns = f.readline()
columns = [item.strip() for item in columns.split(',')]

# Function to produce data with field associativity

def getinfo(columns, rowdata):
    row = [item.strip() for item in rowdata.split(',')]
    return dict(zip(columns, row))

# Function to create an object

def createobj(info): # info is the dictionary created by getinfo()
    print('[DEBUG]:',info)
    s = student.student(info['name'], info['age'], info['regid'])
    s.setmarks('phy', int(info['phy']))
    s.setmarks('chem', int(info['chem']))
    s.setmarks('math', int(info['math']))
    s.setmarks('bio', int(info['bio']))
    return(s)

def assignranks(robjs):
    a = []
    sobjs = robjs
    for obj in sobjs:
        a.append(obj.getaverage())
    a = set(a)
    a = list(a)
    a.sort(reverse=True)
    #print('[DEBUG] Averages',a)
    rank = 1
    for avg in a:
        for obj in sobjs:
            if(obj.getaverage() == avg):
                obj.setrank(rank)
        rank += 1
    return sobjs

def writecsv_report(objs):
    pass

###########################################################################


def classreport(sobjs):
    dottedline = '-'*70
    #template = '{regid:8} | {name:10} | {age:3} | {phy:3} | {chem:3} | {math:3} | {bio:3} | {avg:4} | {rank:2}'
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:2}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for obj in sobjs:
        name = obj.getname()
        age = obj.getage()
        regid = obj.getregid()
        marks = obj.getmarkslist() # dictionary
        avg =  obj.getaverage()
        rank = obj.getrank()
        print(template.format(regid, name, age, marks['phy'], marks['chem'], marks['math'], marks['bio'], avg, rank))
    print(dottedline)

def classreport2file(sobjs, file):
    
    #path = r"C:\Users\Purushotham\Desktop\Clients\HPE\B01\day04\"
    
    fullpath = os.path.join(os.getcwd(), file)
    f = open(fullpath, "w")
    
    dottedline = '-'*70
    #template = '{regid:8} | {name:10} | {age:3} | {phy:3} | {chem:3} | {math:3} | {bio:3} | {avg:4} | {rank:2}'
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:2}'
    f.write('CLASS REPORT' + '\n')
    f.write(dottedline + '\n')
    f.write(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R') + '\n')
    f.write(dottedline + '\n')
    for obj in sobjs:
        name = obj.getname()
        age = obj.getage()
        regid = obj.getregid()
        marks = obj.getmarkslist() # dictionary
        avg =  obj.getaverage()
        rank = obj.getrank()
        f.write(template.format(regid, name, age, marks['phy'], marks['chem'], marks['math'], marks['bio'], avg, rank) + '\n')
    f.write(dottedline + '\n')
    f.close()

###########################################################################

# LAYER #2

from operator import methodcaller

for n in range(7):
    objs.append(createobj(getinfo(columns, f.readline())))


for obj in objs:
    obj.printinfo()


print('Calculating Averages....')
for obj in objs:
    obj.calcaverage()
'''
for obj in objs:
    obj.printinfo()
'''
print('Assigning ranks...')
robjs = assignranks(objs)

'''
for obj in robjs:
    obj.printinfo()
'''
classreport(objs)
classreport2file(objs, 'report.txt')
f.close()
