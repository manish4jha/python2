Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> 
>>> # Declare a list
>>> L = ['red', 'green', 'blue', 12, -23.56, 1/3, True, False, None, ['a','z']]
>>> # Access the elements
>>> # [start:end:interval]
>>> L[0]
'red'
>>> L[1]
'green'
>>> L[-1]
['a', 'z']
>>> L[2:5]
['blue', 12, -23.56]
>>> L[::2]
['red', 'blue', -23.56, True, None]
>>> L[::-1]
[['a', 'z'], None, False, True, 0.3333333333333333, -23.56, 12, 'blue', 'green', 'red']
>>> # Replacability, Mutability
>>> L = ['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1] = 'light-green'
>>> L
['red', 'light-green', 'blue']
>>> L[2]
'blue'
>>> L[2][1]
'l'
>>> L[2][1] = 'L'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    L[2][1] = 'L'
TypeError: 'str' object does not support item assignment
>>> L = ['red', 'green', 'blue', 12, -23.56, 1/3, True, False, None, ['a','z']]
>>> L[-1]
['a', 'z']
>>> L[-1][-1]
'z'
>>> L[-1][-1] = 'j'
>>> L
['red', 'green', 'blue', 12, -23.56, 0.3333333333333333, True, False, None, ['a', 'j']]
>>> # The list is mutable, but the elements in the list need not be mutable
>>> 
>>> 
>>> # OPerators
>>> L1 = ['red', 'green', 'blue']
>>> L2 = ['white', 'grey', 'black']
>>> L1 + L2
['red', 'green', 'blue', 'white', 'grey', 'black']
>>> L1 * 3
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
>>> L3 = (L1 + L2) * 2
>>> L3
['red', 'green', 'blue', 'white', 'grey', 'black', 'red', 'green', 'blue', 'white', 'grey', 'black']
>>> 'orange' in L3
False
>>> 'red' in L3
True
>>> len(L3)
12
>>> L1
['red', 'green', 'blue']
>>> del L1[0]
>>> L
['red', 'green', 'blue', 12, -23.56, 0.3333333333333333, True, False, None, ['a', 'j']]
>>> L1
['green', 'blue']
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> 
>>> # -------------- Functions defined for a list
>>> 
>>> # Adding elements
>>> 
>>> L = ['red', 'green', 'blue']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append('orange')
>>> L
['red', 'green', 'blue', 'yellow', 'orange']
>>> L.insert(3, 'pink')
>>> L
['red', 'green', 'blue', 'pink', 'yellow', 'orange']
>>> 
>>> # ---- some variations
>>> 
>>> L
['red', 'green', 'blue', 'pink', 'yellow', 'orange']
>>> L2
['white', 'grey', 'black']
>>> L[-2]
'yellow'
>>> L[-2] = L2
>>> L
['red', 'green', 'blue', 'pink', ['white', 'grey', 'black'], 'orange']
>>> L = ['red', 'green', 'blue', 'pink', 'yellow', 'orange']
>>> L[-3:-1]
['pink', 'yellow']
>>> L[-3:-1] = L2
>>> L
['red', 'green', 'blue', 'white', 'grey', 'black', 'orange']
>>> L = ['red', 'green', 'blue', 'pink', 'yellow', 'orange']
>>> L[-2:-1]
['yellow']
>>> L[-2]
'yellow'
>>> L[-2:-1] = L2
>>> L
['red', 'green', 'blue', 'pink', 'white', 'grey', 'black', 'orange']
>>> 
>>> 
>>> # Removing elements
>>> 
>>> L
['red', 'green', 'blue', 'pink', 'white', 'grey', 'black', 'orange']
>>> L.pop()
'orange'
>>> L
['red', 'green', 'blue', 'pink', 'white', 'grey', 'black']
>>> L.pop()
'black'
>>> L.pop(3)
'pink'
>>> L
['red', 'green', 'blue', 'white', 'grey']
>>> L.remove('white')
>>> L
['red', 'green', 'blue', 'grey']
>>> 
>>> 
>>> def removefromlist(item, 2):
	
SyntaxError: invalid syntax
>>> def removefromlist(L, item, pos):
	count = 0
	for i in L:
		if(i == item):
			count += 1
			if(count == pos):
				L.remove(i)

				
>>> L
['red', 'green', 'blue', 'grey']
>>> L[3:4] = ['white', 'white', 'white']
>>> L
['red', 'green', 'blue', 'white', 'white', 'white']
>>> L.append('pink')
>>> removefromlist(L, 'white', 2)
>>> L
['red', 'green', 'blue', 'white', 'white', 'pink']
>>> ['red', 'green', 'blue', 'white', 'white', 'white']
['red', 'green', 'blue', 'white', 'white', 'white']
>>> L = ['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
>>> L.remove('white')
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey', 'white']
>>> L = ['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
>>> removefromlist(L, 'white', 2)
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey', 'white']
>>> L = ['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
>>> L
['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
>>> removefromlist(L, 'white', 2)
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey', 'white']
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/remove_exp.py ===
Before:
['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
After: 
['red', 'green', 'blue', 'white', 'black', 'grey', 'white']
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/remove_exp.py ===
Before:
['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
After: 
['red', 'green', 'blue', 'black', 'white', 'grey', 'white']
>>> 
=== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/remove_exp.py ===
Before:
['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
After: 
['red', 'green', 'blue', 'white', 'black', 'white', 'grey']
>>> 
>>> # ---- searching for element
>>> 
>>> L
['red', 'green', 'blue', 'white', 'black', 'white', 'grey']
>>> 'blue' in L
True
>>> L.index('blue')
2
>>> L.count('white')
2
>>> 
>>> # ------ rearrange elements
>>> 
>>> # Reversing
>>> 
>>> L
['red', 'green', 'blue', 'white', 'black', 'white', 'grey']
>>> reversed(L)
<list_reverseiterator object at 0x0000026FA9726E10>
>>> list(reversed(L))
['grey', 'white', 'black', 'white', 'blue', 'green', 'red']
>>> L
['red', 'green', 'blue', 'white', 'black', 'white', 'grey']
>>> L.reverse()
>>> L
['grey', 'white', 'black', 'white', 'blue', 'green', 'red']
>>> 
>>> 
>>> # Sorting
>>> 
>>> L = ['apples', 'zebra', 'cat', 'goat', 'banana']
>>> L
['apples', 'zebra', 'cat', 'goat', 'banana']
>>> sorted(L)
['apples', 'banana', 'cat', 'goat', 'zebra']
>>> L
['apples', 'zebra', 'cat', 'goat', 'banana']
>>> L.sort()
>>> L
['apples', 'banana', 'cat', 'goat', 'zebra']
>>> L.sort(reverse=True)
>>> L
['zebra', 'goat', 'cat', 'banana', 'apples']
>>> 
>>> 
>>> # --------------- copying the lists
>>> 
>>> L
['zebra', 'goat', 'cat', 'banana', 'apples']
>>> L = ['red', 'green', 'blue']
>>> L
['red', 'green', 'blue']
>>> L1 = L
>>> L
['red', 'green', 'blue']
>>> L1
['red', 'green', 'blue']
>>> L1[1] = 'orange'
>>> L1
['red', 'orange', 'blue']
>>> L
['red', 'orange', 'blue']
>>> 
>>> # deep copying
>>> 
>>> import copy
>>> L3 = copy.deepcopy(L)
>>> L
['red', 'orange', 'blue']
>>> L3
['red', 'orange', 'blue']
>>> L3[1] = 'green'
>>> L3
['red', 'green', 'blue']
>>> L
['red', 'orange', 'blue']
>>> L1
['red', 'orange', 'blue']
>>> L.append('yellow')
>>> L
['red', 'orange', 'blue', 'yellow']
>>> L1
['red', 'orange', 'blue', 'yellow']
>>> L3
['red', 'green', 'blue']
>>> 
>>> 
>>> L
['red', 'orange', 'blue', 'yellow']
>>> L1 = L[1:4]
>>> L
['red', 'orange', 'blue', 'yellow']
>>> L1
['orange', 'blue', 'yellow']
>>> L[2] = 'white'
>>> L
['red', 'orange', 'white', 'yellow']
>>> L1
['orange', 'blue', 'yellow']
>>> 
>>> 
>>> L
['red', 'orange', 'white', 'yellow']
>>> L1 = L
>>> L.append('creme')
>>> L
['red', 'orange', 'white', 'yellow', 'creme']
>>> L1
['red', 'orange', 'white', 'yellow', 'creme']
>>> 
>>> L2 = L[:]
>>> L
['red', 'orange', 'white', 'yellow', 'creme']
>>> L2
['red', 'orange', 'white', 'yellow', 'creme']
>>> L2.pop()
'creme'
>>> L
['red', 'orange', 'white', 'yellow', 'creme']
>>> L1
['red', 'orange', 'white', 'yellow', 'creme']
>>> L2
['red', 'orange', 'white', 'yellow']
>>> 
>>> 
>>> 
>>> L1
['red', 'orange', 'white', 'yellow', 'creme']
>>> L1[1]
'orange'
>>> L1[1][::-1]
'egnaro'
>>> 
