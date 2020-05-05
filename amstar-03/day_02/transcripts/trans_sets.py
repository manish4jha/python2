Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ('red', 'green', 'blue')
>>> T1 = ('white', 'grey', 'black')
>>> T + T1
('red', 'green', 'blue', 'white', 'grey', 'black')
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> T
('red', 'green', 'blue')
>>> len(T + T1)
6
>>> 'red' in (T + T1)
True
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T1
>>> T1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> # ------------------------------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> # SETS
>>> 
>>> S = 'mississippi')
SyntaxError: invalid syntax
>>> S = 'mississippi'
>>> list(S)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(S)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(S)
{'p', 'm', 'i', 's'}
>>> 
>>> 
>>> 
>>> s1 = set('abcdef')
>>> s1
{'e', 'c', 'd', 'b', 'f', 'a'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> s2
{'e', 'i', 'j', 'g', 'd', 'h', 'f'}
>>> 
>>> s1 & s2    # intersection
{'f', 'e', 'd'}
>>> s1 | s2    # Union
{'e', 'i', 'j', 'c', 'd', 'b', 'g', 'h', 'f', 'a'}
>>> s1 ^ s2
{'i', 'j', 'c', 'g', 'b', 'h', 'a'}
>>> 
>>> 
>>> s1.add{'x'}
SyntaxError: invalid syntax
>>> s1.add('x')
>>> s1
{'e', 'x', 'c', 'd', 'b', 'f', 'a'}
>>> s1.remove('x')
>>> s1
{'e', 'c', 'd', 'b', 'f', 'a'}
>>> s1.union(s2)
{'e', 'i', 'j', 'c', 'd', 'b', 'g', 'h', 'f', 'a'}
>>> s1.intersection(s2)
{'f', 'e', 'd'}
>>> 
>>> 
>>> 
>>> s2
{'e', 'i', 'j', 'g', 'd', 'h', 'f'}
>>> ls = list(s2)
>>> ls
['e', 'i', 'j', 'g', 'd', 'h', 'f']
>>> ls.sort()
>>> ls
['d', 'e', 'f', 'g', 'h', 'i', 'j']
>>> ''.join(ls)
'defghij'
>>> 
>>> 
>>> 
>>> s3 = { ('a', 'b', 'c'), 'd' , 'e' }
>>> s3
{'d', ('a', 'b', 'c'), 'e'}
>>> s3.add(('x', 'y'))
>>> s3
{('x', 'y'), 'd', ('a', 'b', 'c'), 'e'}
>>> s3.add({'m', 'n'})
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s3.add({'m', 'n'})
TypeError: unhashable type: 'set'
>>> s4 = {'a' , 'b', {'x', 'y'}}
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s4 = {'a' , 'b', {'x', 'y'}}
TypeError: unhashable type: 'set'
>>> 
