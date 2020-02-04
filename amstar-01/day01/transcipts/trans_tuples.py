Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[:]
('red', 'green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> T[0] = 'yellow'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    T[0] = 'yellow'
TypeError: 'tuple' object does not support item assignment
>>> #############################################3
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> T = ['red', 'green', 'blue']
>>> type(T)
<class 'list'>
>>> ##############################################
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> ##################################################
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> ##################################################
>>> L
['red', 'green', 'blue']
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> ###################################################
>>> 
>>> L
['red', 'green', 'blue']
>>> T = tuple(L)
>>> T
('red', 'green', 'blue')
>>> ###################################################
>>> T = ('zebra' , 'cat', 'apple')
>>> sorted(T)
['apple', 'cat', 'zebra']
>>> T
('zebra', 'cat', 'apple')
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> reversed(T)
<reversed object at 0x000001671D42C7B8>
>>> tuple(reversed(T))
('apple', 'cat', 'zebra')
>>> ###################################################
>>> T
('zebra', 'cat', 'apple')
>>> T + ('dog' , 'giraffe')
('zebra', 'cat', 'apple', 'dog', 'giraffe')
>>> T
('zebra', 'cat', 'apple')
>>> T1 = T + ('dog' , 'giraffe')
>>> T1
('zebra', 'cat', 'apple', 'dog', 'giraffe')
>>> 'cat' in T
True
>>> len(T)
3
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T
>>> T
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> ##########################################################
