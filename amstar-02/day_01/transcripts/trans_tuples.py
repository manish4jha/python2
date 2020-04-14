Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue']
>>> type(L)
<class 'list'>
>>> T = ('red', 'green' ,'blue')
>>> type(T)
<class 'tuple'>
>>> T[0]
'red'
>>> T[2]
'blue'
>>> T[-1]
'blue'
>>> T[:]
('red', 'green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> #-------------------
>>> T[0]
'red'
>>> T[0] = 'orange'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    T[0] = 'orange'
TypeError: 'tuple' object does not support item assignment
>>> L
['red', 'green', 'blue']
>>> L[0]
'red'
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue']
>>> T
('red', 'green', 'blue')
>>> 'red' in T
True
>>> T.count('red')
1
>>> T.index('red')
0
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> list(reversed(T))
['blue', 'green', 'red']
>>> # ----------- operators to use on tuple
>>> T
('red', 'green', 'blue')
>>> T1 = ('black', 'white', 'grey')
>>> T + T1
('red', 'green', 'blue', 'black', 'white', 'grey')
>>> T1
('black', 'white', 'grey')
>>> T
('red', 'green', 'blue')
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> len(T + T1)
6
>>> del T1
>>> T1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> # --------------------------------
>>> 
>>> T
('red', 'green', 'blue')
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> T = tuple(L)
>>> T
('red', 'green', 'blue', 'yellow')
>>> 
>>> 
>>> # ----------------------------------
>>> 
>>> L
['red', 'green', 'blue', 'yellow']
>>> T
('red', 'green', 'blue', 'yellow')
>>> r,g,b,y = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
'yellow'
>>> 
>>> 
>>> # --------------------------------
>>> 
>>> T
('red', 'green', 'blue', 'yellow')
>>> T[::-1]
('yellow', 'blue', 'green', 'red')
>>> T[:]
('red', 'green', 'blue', 'yellow')
>>> T[::2]
('red', 'blue')
>>> T[::-1]
('yellow', 'blue', 'green', 'red')
>>> T[::-2]
('yellow', 'green')
>>> 
