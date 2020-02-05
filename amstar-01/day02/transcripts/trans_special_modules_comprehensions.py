Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from operator import itemgetter
>>> itemgetter(1)("apples")
'p'
>>> itemgetter(1)(["apples","banana","cat"])
'banana'
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> f("apples")
'p'
>>> f(["apples","banana","cat"])
'banana'
>>> L = ['zebra', 'cat', 'donkey', 'giraffe', 'yak']
>>> L.sort()
>>> L
['cat', 'donkey', 'giraffe', 'yak', 'zebra']
>>> L.sort(key=itemgetter(-1))
>>> L
['zebra', 'giraffe', 'yak', 'cat', 'donkey']
>>> L.sort(key=itemgetter(-1), reverse=True)
>>> L
['donkey', 'cat', 'yak', 'giraffe', 'zebra']
>>> ############################################################3
>>> from itertools import permutations,combinations
>>> permutations('ABCD', 3)
<itertools.permutations object at 0x000002C8B23198E0>
>>> list(permutations('ABCD', 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations('ABCD', 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> ############################################################
>>> from collections import Counter
>>> L = ['red', 'blue', 'red', 'green', 'blue', 'blue']
>>> D = {}
>>> for color in L:
	if color in D.keys():
		D[color] = D[color] + 1
	else:
		D[color] = 1

		
>>> D
{'red': 2, 'blue': 3, 'green': 1}
>>> z = Counter(L)
>>> z
Counter({'blue': 3, 'red': 2, 'green': 1})
>>> type(z)
<class 'collections.Counter'>
>>> ################################################################
>>> # COMPREHENSIONS
>>> 
>>> LC = [x for x in range(10)]
>>> LC
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L = []
>>> for n in range(1, 101):
	if(n % 3 == 0 and n % 7 == 0):
		L.append(n)

		
>>> L
[21, 42, 63, 84]
>>> LC = [x for x in range(1, 101) if (n % 3 == True) and (n % 7 == 0)]
>>> LC
[]
>>> LC = [x for x in range(1, 101) if (x % 3 == True) and (x % 7 == 0)]
>>> LC
[7, 28, 49, 70, 91]
>>> LC = [x for x in range(1, 101) if (x % 3 == 0) and (x % 7 == 0)]
>>> LC
[21, 42, 63, 84]
>>> x = 9
>>> x % 3 == True
False
>>> T = ( [x, x**2, x**3] for x in range(10) )
>>> T
<generator object <genexpr> at 0x000002C8B23139A8>
>>> list(T)
[[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64], [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512], [9, 81, 729]]
>>> L = ['zebra', 'cat', 'donkey', 'giraffe', 'yak']
>>> D = { elem:len(elem) for elem in L }
>>> D
{'zebra': 5, 'cat': 3, 'donkey': 6, 'giraffe': 7, 'yak': 3}
>>> L = [1,2,3,4]
>>> LC = [x**2 for x in L if (x == 3)]
>>> LC
[9]
>>> LC = [x**2 if x == 3 else x for x in L]
>>> LC
[1, 2, 9, 4]
>>> LC = [ L[x]**2 if x == 2 else L[x] for x in range(len(L))]
>>> LC
[1, 2, 9, 4]
>>> L
[1, 2, 3, 4]
>>> LC = [ (x, y) for x in range(10) for y in range(10) if x + y > 20 ]
>>> LC
[]
>>> LC = [ (x, y) for x in range(10) for y in range(10) if x + y > 12 ]
>>> LC
[(4, 9), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (7, 6), (7, 7), (7, 8), (7, 9), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
>>> 
