Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> L = list(s)
>>> T = tuple(s)
>>> S = set(s)
>>> L
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> T
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> S
{'p', 'm', 'i', 's'}
>>> ######################################################
>>> s1 = set('abcdef')
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i'}
>>> s1
{'c', 'f', 'b', 'd', 'a', 'e'}
>>> s2
{'f', 'h', 'i', 'd', 'g', 'e'}
>>> len(s1)
6
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s1 * 3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1 * 3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> ##### + and * will not work ###########
>>> s1 & s2
{'d', 'f', 'e'}
>>> s1 | s2
{'c', 'f', 'h', 'i', 'b', 'd', 'g', 'a', 'e'}
>>> s1 ^ s2
{'c', 'b', 'h', 'i', 'g', 'a'}
>>> #########################################################
>>> s1.intersection(s2)
{'d', 'f', 'e'}
>>> s1.union(s2)
{'c', 'f', 'h', 'i', 'b', 'd', 'g', 'a', 'e'}
>>> s1
{'c', 'f', 'b', 'd', 'a', 'e'}
>>> s1.add('x')
>>> s1
{'c', 'f', 'b', 'd', 'x', 'a', 'e'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'c', 'f', 'b', 'd', 'x', 'y', 'a', 'e', 'z'}
>>> 'd' in s1
True
>>> s1.remove('d')
>>> s1
{'c', 'f', 'b', 'x', 'y', 'a', 'e', 'z'}
>>> 
