def getvalues(L):
    avg = sum(L)/len(L)
    minval = min(L)
    maxval = max(L)
    return (avg, minval, maxval)

##############################################

print('Enter some numbers: ')
lst = []
uin = ''
while uin != 'q':
    uin = input('# (q to quit)')
    if(uin.isdigit()):
        lst.append(float(uin))

x,y,z = getvalues(lst)
print('--------------------------------')
print('AVERAGE   : ' , x)
print('MINIMUM   : ', y)
print('MAXIMUM   : ', z)
