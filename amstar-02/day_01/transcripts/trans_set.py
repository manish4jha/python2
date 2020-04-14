Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'abcdefg'
>>> s1 = set(s)
>>> s1
{'e', 'b', 'c', 'd', 'f', 'g', 'a'}
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> s1[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1[2]
TypeError: 'set' object is not subscriptable
>>> 'a' in s1
True
>>> len(s1)
7
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> type(s2)
<class 'set'>
>>> s2
{'e', 'j', 'd', 'f', 'g', 'i', 'h'}
>>> # ----------------------------------------------------
>>> 
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> set(s)
{'i', 's', 'm', 'p'}
>>> 
>>> 
>>> L = [1, 2, 3]
>>> s.add(L)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add(L)
AttributeError: 'str' object has no attribute 'add'
>>> s1.add(L)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s1.add(L)
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> # --------------------------------------
>>> 
>>> s1
{'e', 'b', 'c', 'd', 'f', 'g', 'a'}
>>> s2
{'e', 'j', 'd', 'f', 'g', 'i', 'h'}
>>> s1 & s2
{'e', 'g', 'd', 'f'}
>>> s1 | s2
{'e', 'j', 'b', 'd', 'c', 'f', 'g', 'a', 'i', 'h'}
>>> s1 ^ s2
{'j', 'b', 'c', 'i', 'h', 'a'}
>>> s1.intersection(s2)
{'e', 'g', 'd', 'f'}
>>> s1.union(s2)
{'e', 'j', 'b', 'd', 'c', 'f', 'g', 'a', 'i', 'h'}
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'e', 'x', 'b', 'c', 'd', 'f', 'g', 'a'}
>>> s1.add('y')
>>> s1
{'e', 'x', 'b', 'c', 'd', 'f', 'y', 'g', 'a'}
>>> s1.remove('x')
>>> s1
{'e', 'b', 'c', 'd', 'f', 'y', 'g', 'a'}
>>> s1.remove('y')
>>> 
