Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> LT = [1,2,3,'red', 'geen' , 'blue', True, False, 12.5, -45, [1,2,3]]
>>> LT
[1, 2, 3, 'red', 'geen', 'blue', True, False, 12.5, -45, [1, 2, 3]]
>>> type(LT)
<class 'list'>
>>> L1 = ['red', 'green', 'blue']
>>> L2 = ['black', 'grey', 'white']
>>> #############################################
>>> # Operators for working with lists
>>> L1 + L2
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L1
['red', 'green', 'blue']
>>> L2
['black', 'grey', 'white']
>>> L3 = L1 + L3
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    L3 = L1 + L3
NameError: name 'L3' is not defined
>>> L3 = L1 + L2
>>> L3
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L4 = L1 * 3
>>> L4
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
>>> 'red' in L
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    'red' in L
NameError: name 'L' is not defined
>>> 'red' in L1
True
>>> 'black' not in L1
True
>>> L2
['black', 'grey', 'white']
>>> del L[1]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del L[1]
NameError: name 'L' is not defined
>>> del L1[1]
>>> L1
['red', 'blue']
>>> del L2[1]
>>> L2
['black', 'white']
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> L2
['black', 'white']
>>> ######################################################
>>> # Accessing and replacing elements in list
>>> L = ['red', 'green', 'blue']
>>> L = ['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> len(L)
6
>>> L
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L[0]
'red'
>>> L[-1]
'white'
>>> L[-2]
'grey'
>>> L[len(L) - 1]
'white'
>>> L[1:4]
['green', 'blue', 'black']
>>> L[:4]
['red', 'green', 'blue', 'black']
>>> L[4:]
['grey', 'white']
>>> L[:]
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L[::2]
['red', 'blue', 'grey']
>>> L[::-1]
['white', 'grey', 'black', 'blue', 'green', 'red']
>>> L
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> L[-1] = 'sparkling white'
>>> L
['red', 'green', 'blue', 'black', 'grey', 'sparkling white']
>>> L[1][1] = 'R'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    L[1][1] = 'R'
TypeError: 'str' object does not support item assignment
>>> ######################################################
>>> # How to add elements to a list?
>>> L
['red', 'green', 'blue', 'black', 'grey', 'sparkling white']
>>> L.append('orange')
>>> L
['red', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange']
>>> L.append('pink')
>>> L
['red', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L.insert(1, 'yellow')
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L3 = ['cyan', 'magenta']
>>> L.append(L3)
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink', ['cyan', 'magenta']]
>>> L.pop()
['cyan', 'magenta']
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L + L3
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta']
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L.extend(L3)
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta']
>>> # How to remove elements?
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta']
>>> L.pop()
'magenta'
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink', 'cyan']
>>> L.pop()
'cyan'
>>> L
['red', 'yellow', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L.pop(1)
'yellow'
>>> L
['red', 'green', 'blue', 'black', 'grey', 'sparkling white', 'orange', 'pink']
>>> L.pop(L.index('grey'))
'grey'
>>> L
['red', 'green', 'blue', 'black', 'sparkling white', 'orange', 'pink']
>>> L.remove('blue')
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink']
>>> ###############################################################
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink']
>>> L3
['cyan', 'magenta']
>>> L.extend(L3)
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta']
>>> ###############################################################
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta']
>>> 'red' in L
True
>>> L.index('red')
0
>>> L.find('red')
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    L.find('red')
AttributeError: 'list' object has no attribute 'find'
>>> L.extend(['red'] * 3)
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta', 'red', 'red', 'red']
>>> L.count('red')
4
>>> L.index('maroon')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    L.index('maroon')
ValueError: 'maroon' is not in list
>>> if 'maroon' in L:
	L.index('maroon')

	
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta', 'red', 'red', 'red']
>>> L.index('red')
0
>>> L[1:].index('red')
7
>>> ############################################################
>>> # Sort
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta', 'red', 'red', 'red']
>>> L1 = ['zebra', 'cat', 'apples', 'dog', 'monkey']
>>> sorted(L1)
['apples', 'cat', 'dog', 'monkey', 'zebra']
>>> L1
['zebra', 'cat', 'apples', 'dog', 'monkey']
>>> L11 = sorted(L1)
>>> L11
['apples', 'cat', 'dog', 'monkey', 'zebra']
>>> L1.sort()
>>> L1
['apples', 'cat', 'dog', 'monkey', 'zebra']
>>> L1.sort(reverse=True)
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> L1 = ['zebra', 'cat', 'apples', 'dog', 'monkey']
>>> L[3]
'sparkling white'
>>> L1[3]
'dog'
>>> L1.sort()
>>> L1[3]
'monkey'
>>> # Reverse
>>> L
['red', 'green', 'black', 'sparkling white', 'orange', 'pink', 'cyan', 'magenta', 'red', 'red', 'red']
>>> L1
['apples', 'cat', 'dog', 'monkey', 'zebra']
>>> reversed(L1)
<list_reverseiterator object at 0x000002DF17A9EF98>
>>> list(reversed(L1))
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> L1
['apples', 'cat', 'dog', 'monkey', 'zebra']
>>> L1.reverse()
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> ##########################################################
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> L2 = L1
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> L2
['zebra', 'monkey', 'dog', 'cat', 'apples']
>>> L1.append('donkey')
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey']
>>> L2
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey']
>>> from copy import deepcopy
>>> L3 = deepcopy(L1)
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey']
>>> L3
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey']
>>> L1.append('giraffe')
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L3
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey']
>>> L2
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L4 = L1[:]
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L4
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L1.append('lion')
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe', 'lion']
>>> L4
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe']
>>> L5 = list(L1)
>>> L5
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe', 'lion']
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe', 'lion']
>>> L1.append('tiger')
>>> L1
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe', 'lion', 'tiger']
>>> L5
['zebra', 'monkey', 'dog', 'cat', 'apples', 'donkey', 'giraffe', 'lion']
>>> L6 = ['red', 'green', 'blue', ['black']]
>>> L7 = L6[:]
>>> L7
['red', 'green', 'blue', ['black']]
>>> L6
['red', 'green', 'blue', ['black']]
>>> L6[-1].append('white')
>>> L6
['red', 'green', 'blue', ['black', 'white']]
>>> L7
['red', 'green', 'blue', ['black', 'white']]
>>> L6.append('grey')
>>> L6
['red', 'green', 'blue', ['black', 'white'], 'grey']
>>> L7
['red', 'green', 'blue', ['black', 'white']]
>>> L7[-1].apeend('cyan')
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    L7[-1].apeend('cyan')
AttributeError: 'list' object has no attribute 'apeend'
>>> L7[-1].append('cyan')
>>> L6
['red', 'green', 'blue', ['black', 'white', 'cyan'], 'grey']
>>> L7
['red', 'green', 'blue', ['black', 'white', 'cyan']]
>>> ######### Glenn's question
>>> L6 = ['red', 'green', 'blue', ['black']]
>>> L7 = list(L6)
>>> L7
['red', 'green', 'blue', ['black']]
>>> L7.append('grey')
>>> L7
['red', 'green', 'blue', ['black'], 'grey']
>>> L6
['red', 'green', 'blue', ['black']]
>>> L6[-1].append('blue')
>>> L6
['red', 'green', 'blue', ['black', 'blue']]
>>> L7
['red', 'green', 'blue', ['black', 'blue'], 'grey']
>>> ##################### deepcopy method
>>> L6 = ['red', 'green', 'blue', ['black']]
>>> L7 = deepcopy(L6)
>>> L6
['red', 'green', 'blue', ['black']]
>>> L6.append('grey')
>>> L6
['red', 'green', 'blue', ['black'], 'grey']
>>> L7
['red', 'green', 'blue', ['black']]
>>> L7[-1].append('blue')
>>> L7
['red', 'green', 'blue', ['black', 'blue']]
>>> L6
['red', 'green', 'blue', ['black'], 'grey']
>>> 
