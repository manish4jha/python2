Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue']
>>> T = ('red', 'green', 'blue')
>>> type(L)
<class 'list'>
>>> type(T)
<class 'tuple'>
>>> T
('red', 'green', 'blue')
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[:]
('red', 'green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> 
>>> 
>>> T[0] = 'green'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    T[0] = 'green'
TypeError: 'tuple' object does not support item assignment
>>> L[0] = 'green'
>>> L
['green', 'green', 'blue']
>>> T
('red', 'green', 'blue')
>>> 
>>> 
>>> T
('red', 'green', 'blue')
>>> sorted(T)
['blue', 'green', 'red']
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> reversed(T)
<reversed object at 0x000001F418C11470>
>>> list(reversed(T))
['blue', 'green', 'red']
>>> 
>>> 
>>> 
>>> T
('red', 'green', 'blue')
>>> LT = list(T)
>>> Lt
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    Lt
NameError: name 'Lt' is not defined
>>> LT
['red', 'green', 'blue']
>>> LT.append('yellow')
>>> LT
['red', 'green', 'blue', 'yellow']
>>> T
('red', 'green', 'blue')
>>> TM = tuple(LT)
>>> TM
('red', 'green', 'blue', 'yellow')
>>> ('red', 'green', 'blue', 'yellow')
('red', 'green', 'blue', 'yellow')

>>> ###
>>> 
>>> T1 = 1,2,3,4,5
>>> T1
(1, 2, 3, 4, 5)
>>> r,g,b,y = T
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    r,g,b,y = T
ValueError: not enough values to unpack (expected 4, got 3)
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> r,g,b = TM
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    r,g,b = TM
ValueError: too many values to unpack (expected 3)
>>> r,g,*b = TM
>>> r
'red'
>>> g
'green'
>>> b
['blue', 'yellow']
>>> # -------------------------
>>> 
>>> 
>>> 
>>> 
>>> T
('red', 'green', 'blue')
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> TM
('red', 'green', 'blue', 'yellow')
>>> r,g,b = TM
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    r,g,b = TM
ValueError: too many values to unpack (expected 3)
>>> type(r)
<class 'str'>
>>> r,g,*b = TM
>>> r
'red'
>>> g
'green'
>>> b
['blue', 'yellow']
>>> type(b)
<class 'list'>
>>> 
