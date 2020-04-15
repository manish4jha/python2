Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Modules
>>> # functools, itertools, operator, collection
>>> from functools import reduce
>>> f = lambda x, y : x + y
>>> f(10, 20)
30
>>> L = [1,2,3,4]
>>> reduce(f, L)
10
>>> # 1 + 2 = 3
>>> # 3 + 3 = 6
>>> # 6 + 4 = 10
>>> 
>>> T = ('apples', 'ball', 'coconut' ,'donkey')
>>> s = ''
>>> for item in T:
	s += item

	
>>> print(s)
applesballcoconutdonkey
>>> set(s)
{'s', 'b', 'c', 'n', 't', 'y', 'p', 'e', 'k', 'l', 'd', 'o', 'u', 'a'}
>>> reduce(lambda s1, s2 : ''.join(list(set(s1) | set(s2))), T)
'lsbcnypektdoua'
>>> list(reduce(lambda s1, s2 : ''.join(list(set(s1) | set(s2))), T).sort()

     )
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(reduce(lambda s1, s2 : ''.join(list(set(s1) | set(s2))), T).sort()
AttributeError: 'str' object has no attribute 'sort'
>>> list(reduce(lambda s1, s2 : ''.join(list(set(s1) | set(s2))), T)).sort()
>>> 
>>> list(reduce(lambda s1, s2 : ''.join(list(set(s1) | set(s2))), T))
['l', 's', 'b', 'c', 'n', 'y', 'p', 'e', 'k', 't', 'd', 'o', 'u', 'a']
>>> 
>>> 
>>> # -------- collections
>>> 
>>> from collections import Counter
>>> L = ['red', 'green', 'blue', 'red', 'blue', 'red']
>>> D = {}
>>> for word in L:
	if word in D.keys():
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'red': 3, 'green': 1, 'blue': 2}
>>> 
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'blue': 2, 'green': 1})
>>> 
>>> import collections
>>> y = collections.Counter(L)
>>> y
Counter({'red': 3, 'blue': 2, 'green': 1})
>>> 
>>> 
>>> 
>>> # --------------- itertools
>>> 
>>> from itertools import permutations, combinations
>>> s = 'ABCD'
>>> permutations(s, 3)
<itertools.permutations object at 0x000001A4693D44C0>
>>> list(permutations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> 
>>> for p in permutations('ABCD', 3):
	print(str(p), end=', ')

	
('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B'), 
>>> for p in permutations('ABCD', 3):
	print(''.join(p), end=', ')

	
ABC, ABD, ACB, ACD, ADB, ADC, BAC, BAD, BCA, BCD, BDA, BDC, CAB, CAD, CBA, CBD, CDA, CDB, DAB, DAC, DBA, DBC, DCA, DCB, 
>>> 
>>> 
>>> # ---------- operator

>>> itemgetter(1)('apples')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    itemgetter(1)('apples')
NameError: name 'itemgetter' is not defined
>>> from operator import itemgetter
>>> itemgetter(1)('apples')
'p'
>>> itemgetter(1)(['red', 'green', 'blue'])
'green'
>>> itemgetter(1)((('red', 1), ('green', 2), ('blue',3)))
('green', 2)
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> f(['red', 'green', 'blue'])
'green'
>>> f('apples')
'p'
>>> L = ['zebra', 'donkey', 'horse', 'ant']
>>> L.sort()
>>> L
['ant', 'donkey', 'horse', 'zebra']
>>> L.sort(key=itemgetter(-1))
>>> L
['zebra', 'horse', 'ant', 'donkey']
>>> L.sort(key=itemgetter(1))
>>> L
['zebra', 'ant', 'horse', 'donkey']
>>> 
