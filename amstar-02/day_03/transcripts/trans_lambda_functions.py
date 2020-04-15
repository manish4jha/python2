Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lambda x,y : x+y
<function <lambda> at 0x000001439A802620>
>>> f = lambda x,y : x+y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> def add2(x, y):
	return x + y

>>> add_2 = lambda x,y : x+y
>>> L = ['giraffe', 'zebra', 'monkey', 'goat', 'lion']
>>> L.sort()
>>> L
['giraffe', 'goat', 'lion', 'monkey', 'zebra']
>>> L.sort(key=lambda s:s[-1])
>>> L
['zebra', 'giraffe', 'lion', 'goat', 'monkey']
>>> ### basic ==> lambda inputs : outputs
>>> 
>>> f = lambda s : s[-1]
>>> f('giraffe')
'e'
>>> L = ['Giraffe', 'zebra', 'Monkey', 'goat', 'lion']
>>> L.sort()
>>> L
['Giraffe', 'Monkey', 'goat', 'lion', 'zebra']
>>> def changecase(x):
	return x.lower()

>>> L.sort(key=changecase)
>>> L
['Giraffe', 'goat', 'lion', 'Monkey', 'zebra']
>>> L = ['Giraffe', 'zebra', 'Monkey', 'goat', 'lion']
>>> L.sort(key=lambda x : x.lower())
>>> l
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
['Giraffe', 'goat', 'lion', 'Monkey', 'zebra']
>>> 
