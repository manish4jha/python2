# Question from Mr. Sathish Kumar


a,b=0,1
print('[Debug]: a = %d b = %d' % (a, b))
print('-----')
while b < 1000:
    print(b,end = ' ',flush = True)
    a,b = b,a+b
    print('\n[Debug]: a = %d b = %d' % (a, b))
    


'''
# ------------------------
# 0 1 1 2 3 5 8 13...

a = 0
b = 1
while b < 1000:
    c = a + b
    print(c, end = ' ')
    #a,b = b,a+b # Simultaneous RHS calculations

    a = b
    b = c

# ----------------------------

a,b = b,a+b

a = b
b = a + b
'''


>>> T = ('red', 'green', 'blue')
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> T = 'red', 'green', 'blue', 'yellow'
>>> type(T)
<class 'tuple'>
>>> T
('red', 'green', 'blue', 'yellow')
>>> r,g,b,y = T
>>> r,g,b,y = 'red', 'green', 'blue', 'yellow'
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
'yellow'
>>> 
