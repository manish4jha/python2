Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> 
>>> # <iterator> ----> string, list, tuple, set, dictionary
>>> 
>>> s = 'vibgyor'
>>> for ch in s:
	print(ch.upper())

	
V
I
B
G
Y
O
R
>>> for color in ['red', 'green', 'blue']:
	print(color, ' ------> ', len(color))

	
red  ------>  3
green  ------>  5
blue  ------>  4
>>> for color in ('red', 'green', 'blue'):
	print(color, ' ------> ', len(color))for color in ['red', 'green', 'blue']:
		print(color, ' ------> ', len(color))
		
SyntaxError: invalid syntax
>>> for color in ('red', 'green', 'blue'):
	print(color, ' ------> ', len(color))

	
red  ------>  3
green  ------>  5
blue  ------>  4
>>> for i in set('abcdefg'):
	print(i, end=' ')

	
f d b a g c e 
>>> D = {'name':'Anil', 'age':35, 'country': 'India', 'company':'Oracle'}
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> for item in D:
	print(item)

	
name
age
country
company
>>> for item in D.values():
	print(item)

	
Anil
35
India
Oracle
>>> for item in D.keys():
	print(item, end='>')

	
name>age>country>company>
>>> for item in D.items():
	print(item)

	
('name', 'Anil')
('age', 35)
('country', 'India')
('company', 'Oracle')
>>> for key, value in D.items():
	print(key, ' --> ', value)

	
name  -->  Anil
age  -->  35
country  -->  India
company  -->  Oracle
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> D1 = {}
>>> for key, value in D.items():
	D1.setdefault(value, key)

	
'name'
'age'
'country'
'company'
>>> D1
{'Anil': 'name', 35: 'age', 'India': 'country', 'Oracle': 'company'}
>>> 
>>> colors = ['red', 'green', 'blue']
>>> # D = {'red':{'length':3, 'r':1, 'e':1, 'd':1 }}
>>> 
>>> D = {}
>>> for color in colors:
	D[color] = None

	
>>> D
{'red': None, 'green': None, 'blue': None}
>>> len('red')
3
>>> s = 'red'
>>> for ch in set('green'):
	pass

>>> s = 'green'
>>> for ch in set(s):
	print(ch, ' occurs ', s.count(ch), ' times ')

	
r  occurs  1  times 
n  occurs  1  times 
g  occurs  1  times 
e  occurs  2  times 
>>> for ch in set(s):
	print(ch, ' occurs ', s.count(ch), ' times ')

	
r  occurs  1  times 
n  occurs  1  times 
g  occurs  1  times 
e  occurs  2  times 
>>> D2 = {}
>>> for ch in set(s):
	D2.setdefault(ch, s.count(ch))

	
1
1
1
2
>>> D2
{'r': 1, 'n': 1, 'g': 1, 'e': 2}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/for_loop_aaplication.py 
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle/day_02/code/for_loop_aaplication.py", line 9, in <module>
    D2.setdefault(ch, s.count(ch))
NameError: name 's' is not defined
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/for_loop_aaplication.py 
{'red': {'length': 3, 'r': 1, 'e': 1, 'd': 1}, 'green': {'length': 5, 'n': 1, 'g': 1, 'e': 2, 'r': 1}, 'blue': {'length': 4, 'b': 1, 'l': 1, 'u': 1, 'e': 1}}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/for_loop_aaplication.py 
{'computer': {'length': 8, 'c': 1, 'm': 1, 'o': 1, 'r': 1, 'p': 1, 'u': 1, 't': 1, 'e': 1}, 'laptop': {'length': 6, 'l': 1, 'o': 1, 'a': 1, 'p': 2, 't': 1}, 'mobile': {'length': 6, 'm': 1, 'b': 1, 'l': 1, 'o': 1, 'i': 1, 'e': 1}, 'desktop': {'length': 7, 'k': 1, 'o': 1, 's': 1, 'p': 1, 'd': 1, 't': 1, 'e': 1}}
>>> 
>>> 
>>> 
>>> # -------------------- WHILE LOOP
>>> 
>>> i = 0
>>> while i <= 10:
	print(i, i**2, i**3)
	i = i + 1

	
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
>>> 
>>> 
>>> # ------------------------- Loop controls
>>> 
>>> # break statement
>>> 
>>> s = 'computer'
>>> for char in s:
	print(char.upper(), end='*')

	
C*O*M*P*U*T*E*R*
>>> for char in s:
	if(char == 'u'):
		break   # Exits from the loop
	else:
		print(char.upper(), end='*')

		
C*O*M*P*
>>> for char in s:
	if(char == 'u'):
		continue   # skip to the next iteration
	else:
		print(char.upper(), end='*')

		
C*O*M*P*T*E*R*
>>> for char in s:
	if(char == 'u'):
		print('X')
		pass   # Don't do anything
	else:
		print(char.upper(), end='*')

		
C*O*M*P*X
T*E*R*
>>> for char in s:
	if(char == 'u'):
		continue   # skip to the next iteration
	
	print(char.upper(), end='*')

	
C*O*M*P*T*E*R*
>>> for char in s:
	if(char == 'u'):
		pass   	
	print(char.upper(), end='*')

	
C*O*M*P*U*T*E*R*
>>> 
>>> 
>>> 
>>> # --------------------------------- LOOP ELSE BLOCKS
>>> 
>>> # see loop_else_block_demo.py
>>> 
>>> for n in [1,2,3,4]:
	print(n**2)

	
1
4
9
16
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(20, 30, 2))
[20, 22, 24, 26, 28]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/loop_else_block_demo.py 
Enter a number: 12
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/loop_else_block_demo.py 
Enter a number: 13
The number is prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/loop_else_block_demo.py 
Enter a number: 12
The number is not prime
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/loop_else_block_demo.py 
Enter a number: 13
The number is prime
>>> 
