Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> L = ['red', 'green', 'blue', 34, 56, 67, True, False, ['a', 'e', 'i']]
>>> # Acess the elements
>>> L[0]
'red'
>>> L[1]
'green'
>>> L[-1]
['a', 'e', 'i']
>>> L[-1][1]
'e'
>>> L[1:4]
['green', 'blue', 34]
>>> L[::2]
['red', 'blue', 56, True, ['a', 'e', 'i']]
>>> # Replace elements
>>> L[0]
'red'
>>> L[0] = 'Orange'
>>> L
['Orange', 'green', 'blue', 34, 56, 67, True, False, ['a', 'e', 'i']]
>>> L[-1][1] ='E'
>>> L
['Orange', 'green', 'blue', 34, 56, 67, True, False, ['a', 'E', 'i']]
>>> L[0]
'Orange'
>>> L[0][2]
'a'
>>> L[0][2] = 'A'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    L[0][2] = 'A'
TypeError: 'str' object does not support item assignment
>>> L[-1]
['a', 'E', 'i']
>>> L[-1].append('o')
>>> L
['Orange', 'green', 'blue', 34, 56, 67, True, False, ['a', 'E', 'i', 'o']]
>>> L1 = ['Orange', 'green', 'blue']
>>> L1[0]
'Orange'
>>> L1[1]
'green'
>>> L1[2]
'blue'
>>> L1[-1]
'blue'
>>> L[-1]
['a', 'E', 'i', 'o']
>>> L[-2]
False
>>> L1[-2]
'green'
>>> L1[-3]
'Orange'
>>> L
['Orange', 'green', 'blue', 34, 56, 67, True, False, ['a', 'E', 'i', 'o']]
>>> L[1]
'green'
>>> L[1] = ['pink', 'yellow']
>>> L
['Orange', ['pink', 'yellow'], 'blue', 34, 56, 67, True, False, ['a', 'E', 'i', 'o']]
>>> L[3:6] = ['black', 'white', 'grey']
>>> L
['Orange', ['pink', 'yellow'], 'blue', 'black', 'white', 'grey', True, False, ['a', 'E', 'i', 'o']]
>>> # Operators
>>> L1 = ['a', 'b', 'c']
>>> L2 = [1, 2, 3]
>>> L1 + L2
['a', 'b', 'c', 1, 2, 3]
>>> L2 + L1 + L2
[1, 2, 3, 'a', 'b', 'c', 1, 2, 3]
>>> L1
['a', 'b', 'c']
>>> L2
[1, 2, 3]
>>> L1 * 5
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
>>> 'a' in L1 + L2
True
>>> 5 in L1 + L2
False
>>> len(L1)
3
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> # List -> add elements, remove elements, re-arrange, search
>>> # iteration -> loops -> next session
>>> l = ['red', 'green', 'blue']
>>> # adding elements
>>> l.append('orange')
>>> l
['red', 'green', 'blue', 'orange']
>>> l.append('pink')
>>> l
['red', 'green', 'blue', 'orange', 'pink']
>>> l.insert(3, 'yellow')
>>> l
['red', 'green', 'blue', 'yellow', 'orange', 'pink']
>>> l1 = ['cyan', 'magenta']
>>> l.append(l1)
>>> l
['red', 'green', 'blue', 'yellow', 'orange', 'pink', ['cyan', 'magenta']]
>>> l = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
>>> l + L1
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l + L1
NameError: name 'L1' is not defined
>>> l + l1
['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'cyan', 'magenta']
>>> l
['red', 'green', 'blue', 'yellow', 'orange', 'pink']
>>> l.extend(l1)
>>> l
['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'cyan', 'magenta']
>>> l.append(l1[0])
>>> l
['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan']
>>> # ---------------------------
>>> l = ['red', 'green', 'blue']
>>> l1 = ['yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan']
>>> l[2:2] = l1
>>> l
['red', 'green', 'yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan', 'blue']
>>> l = ['red', 'green', 'blue']
>>> l[2] = l1
>>> l
['red', 'green', ['yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan']]
>>> l = ['red', 'green', 'blue']
>>> l.insert(2, l1)
>>> l
['red', 'green', ['yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan'], 'blue']
>>> # ------------ questions -----------##
>>> 
>>> 
>>> l = ['yellow', 'orange', 'pink', 'cyan', 'magenta', 'cyan']
>>> # deleting elements
>>> l.pop()
'cyan'
>>> l
['yellow', 'orange', 'pink', 'cyan', 'magenta']
>>> l.pop()
'magenta'
>>> l
['yellow', 'orange', 'pink', 'cyan']
>>> l.pop(1)
'orange'
>>> l
['yellow', 'pink', 'cyan']
>>> l.remove('pink')
>>> l
['yellow', 'cyan']
>>> mat = [[1,2,3], [3,4,5], [5,6,7]]
>>> mat[0][1]
2
>>> mat[1][0]
3
>>> mat[1].remove(3)
>>> mat
[[1, 2, 3], [4, 5], [5, 6, 7]]
>>> 
>>> 
>>> # rearranging elements of a list
>>> 
>>> L = ['apples' ,'grapes', 'cherries', 'bananas']
>>> reversed(L)
<list_reverseiterator object at 0x0000024863177358>
>>> list(reversed(L))
['bananas', 'cherries', 'grapes', 'apples']
>>> L
['apples', 'grapes', 'cherries', 'bananas']
>>> L.reverse()
>>> L
['bananas', 'cherries', 'grapes', 'apples']
>>> L
['bananas', 'cherries', 'grapes', 'apples']
>>> sorted(L)
['apples', 'bananas', 'cherries', 'grapes']
>>> L
['bananas', 'cherries', 'grapes', 'apples']
>>> L.sort()
>>> L
['apples', 'bananas', 'cherries', 'grapes']
>>> L = [2,5,3,7,1,4]
>>> L.sort()
>>> L
[1, 2, 3, 4, 5, 7]
>>> L = [2,5,3,7,1,4]
>>> L.sort(reverse=True)
>>> L
[7, 5, 4, 3, 2, 1]
>>> L = ['bananas', 'cherries', 'grapes', 'apples']
>>> sorted(L, reverse=True)
['grapes', 'cherries', 'bananas', 'apples']
>>> 
>>> 
>>> L
['bananas', 'cherries', 'grapes', 'apples']
>>> L.sort()
>>> L
['apples', 'bananas', 'cherries', 'grapes']
>>> L.sort(reverse=True)
>>> L
['grapes', 'cherries', 'bananas', 'apples']
>>> print(L)
['grapes', 'cherries', 'bananas', 'apples']
>>> 
>>> 
>>> # search
>>> 
>>> L
['grapes', 'cherries', 'bananas', 'apples']
>>> 'apples' in L
True
>>> L.index('cherries')
1
>>> L.append('grapes')
>>> L.count('grapes')
2
>>> L
['grapes', 'cherries', 'bananas', 'apples', 'grapes']
>>> L.index('grapes')
0
>>> L.find('grapes')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    L.find('grapes')
AttributeError: 'list' object has no attribute 'find'
>>> 
>>> # ---------- don't try to understand here
>>> 
>>> def searchlist(L, elem):
	print("Number of occurances: ", L.count(elem))
	index = 0
	for e in L:
		if(e == elem):
			print(e + ' found in ' + index)

			
>>> L
['grapes', 'cherries', 'bananas', 'apples', 'grapes']
>>> searchlist(L, 'grapes')
Number of occurances:  2
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    searchlist(L, 'grapes')
  File "<pyshell#151>", line 6, in searchlist
    print(e + ' found in ' + index)
TypeError: can only concatenate str (not "int") to str
>>> def searchlist(L, elem):
	print("Number of occurances: ", L.count(elem))
	index = 0
	for e in L:
		if(e == elem):
			print(e + ' found in ' + str(index))

			
>>> searchlist(L, 'grapes')
Number of occurances:  2
grapes found in 0
grapes found in 0
>>> def searchlist(L, elem):
	print("Number of occurances: ", L.count(elem))
	index = 0
	for e in L:
		if(e == elem):
			print(e + ' found in ' + str(index))
		index += 1

		
>>> searchlist(L, 'grapes')
Number of occurances:  2
grapes found in 0
grapes found in 4
>>> L.insert(3, 'grapes')
>>> searchlist(L, 'grapes')
Number of occurances:  3
grapes found in 0
grapes found in 3
grapes found in 5
>>> 
>>> 
>>> # ---------------------------------------------------------------
>>> 
>>> 

>>> L = ['red', 'green', 'blue']
>>> L1 = L
>>> L
['red', 'green', 'blue']
>>> L1
['red', 'green', 'blue']
>>> L1.append('yellow')
>>> L1
['red', 'green', 'blue', 'yellow']
>>> L
['red', 'green', 'blue', 'yellow']
>>> # L and L1 points to the same location
>>> 
>>> from copy import deepcopy
>>> # import copy
>>> L3 = deepcopy(L1)
>>> L1
['red', 'green', 'blue', 'yellow']
>>> L3
['red', 'green', 'blue', 'yellow']
>>> L3.append('orange')
>>> L3
['red', 'green', 'blue', 'yellow', 'orange']
>>> L1
['red', 'green', 'blue', 'yellow']
>>> L2
[1, 2, 3]
>>> L
['red', 'green', 'blue', 'yellow']
>>> L
['red', 'green', 'blue', 'yellow']
>>> L1
['red', 'green', 'blue', 'yellow']
>>> L3
['red', 'green', 'blue', 'yellow', 'orange']
>>> 
