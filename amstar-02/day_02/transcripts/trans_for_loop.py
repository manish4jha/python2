Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue']
>>> for color in L:
	print(color)

	
red
green
blue
>>> for ch in 'python':
	print(ch)

	
p
y
t
h
o
n
>>> for item in ('white', 'grey', 'black'):
	print(item.upper())

	
WHITE
GREY
BLACK
>>> s = set('apples')
>>> s
{'e', 'l', 'a', 's', 'p'}
>>> for i in s:
	print(i, end=' ')

	
e l a s p 
>>> D = {'name':'Anil', 'age':35, 'country':'India', 'company':'oracle' }
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'oracle'}
>>> for item in D:
	print(item)

	
name
age
country
company
>>> for value in D.values():
	print(value)

	
Anil
35
India
oracle
>>> for pair in D.items():
	print(pair)

	
('name', 'Anil')
('age', 35)
('country', 'India')
('company', 'oracle')
>>> # ---------------------------------
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'oracle'}
>>> 
>>> for key, value in D.items():
	print(key, value)

	
name Anil
age 35
country India
company oracle
>>> D1 = {}
>>> for key, value in D.items():
	D1.setdefault(value, key)

	
'name'
'age'
'country'
'company'
>>> D1
{'Anil': 'name', 35: 'age', 'India': 'country', 'oracle': 'company'}
>>> D1.setdefault('mysore', 'native')
'native'
>>> D1
{'Anil': 'name', 35: 'age', 'India': 'country', 'oracle': 'company', 'mysore': 'native'}
>>> 
>>> # ------------------------ consecutive numbers
>>> 
>>> N = [1,2,3,4,5]
>>> for n in N:
	print(n**2)

	
1
4
9
16
25
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 70))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
>>> list(range(1, 100, 3))
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97]
>>> 
>>> for n in range(10, 100):
	print(n)

	
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> L = []
>>> for n in range(10, 100):
	sn = str(n)
	check = int(sn[1]) + int(sn[0])
	if(check == 7):
		L.append(n)

		
>>> L
[16, 25, 34, 43, 52, 61, 70]
>>> n = 65
>>> sn = str(n)
>>> sn
'65'
>>> type(sn)
<class 'str'>
>>> sn[1]
'5'
>>> sn[0]
'6'
>>> sn[1] + sn[0]
'56'
>>> int(sn[1]) + int(sn[0])
11
>>> int(sn[0]) + int(sn[1])
11
>>> 
