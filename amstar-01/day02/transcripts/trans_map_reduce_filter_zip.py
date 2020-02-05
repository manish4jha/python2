Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # lambda <inputs> : <outputs>
>>> lambda a,b : a + b
<function <lambda> at 0x0000022D990FD598>
>>> f = lambda a,b : a + b
>>> f
<function <lambda> at 0x0000022D990FD620>
>>> type(f)
<class 'function'>
>>> f(10, 10)
20
>>> f(20, 45)
65
>>> f("100", "220")
'100220'
>>> def add2(a, b):
	return a + b

>>> add2(20, 45)
65
>>> add2("100", "220")
'100220'
>>> f2 = lambda a : a.upper()
>>> f2("python")
'PYTHON'
>>> ###################################################
>>> temp = [10, 20, 45, 90, 100] # Temperatures in celcius
>>> def c2f(t):
	return t * 1.8 + 32

>>> c2f(100)
212.0
>>> temp_f = []
>>> for t in temp:
	temp_f.append(c2f(t))

	
>>> temp_f
[50.0, 68.0, 113.0, 194.0, 212.0]
>>> temp_f2 = map(c2f, temp)
>>> temp_f2
<map object at 0x0000022D990AC978>
>>> list(temp_f2)
[50.0, 68.0, 113.0, 194.0, 212.0]
>>> temp_f3 = map(lambda t : t * 1.8 + 32, temp)
>>> temp_f3
<map object at 0x0000022D99101908>
>>> list(temp_f3)
[50.0, 68.0, 113.0, 194.0, 212.0]
>>> t = 10
>>> temp_f4 = map(lambda t : t * 1.8 + 32, t)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    temp_f4 = map(lambda t : t * 1.8 + 32, t)
TypeError: 'int' object is not iterable
>>> t = [10,]
>>> temp_f4 = map(lambda t : t * 1.8 + 32, t)
>>> temp_f4
<map object at 0x0000022D99128EF0>
>>> list(temp_f4)
[50.0]
>>> ################################################################
>>> 
>>> # filter()
>>> 
>>> import random
>>> rn = []
>>> for i in range(100):
	rn.append(random.randint(1, 100))

	
>>> rn
[70, 17, 79, 89, 64, 91, 65, 35, 96, 29, 35, 44, 70, 88, 28, 80, 98, 70, 18, 80, 57, 47, 23, 91, 78, 91, 98, 44, 40, 6, 40, 56, 99, 79, 62, 30, 67, 74, 10, 90, 10, 51, 90, 82, 91, 52, 81, 35, 23, 71, 30, 7, 24, 9, 67, 67, 96, 47, 69, 2, 64, 70, 38, 32, 43, 25, 82, 91, 52, 26, 96, 82, 18, 12, 96, 35, 84, 98, 84, 89, 53, 17, 5, 12, 87, 55, 22, 13, 62, 85, 42, 13, 17, 36, 2, 98, 97, 7, 5, 47]
>>> l_div3 = filter(lambda n : (n % 3 == 0), rn)
>>> l_div3
<filter object at 0x0000022D99128A90>
>>> list(l_div3)
[96, 18, 57, 78, 6, 99, 30, 90, 51, 90, 81, 30, 24, 9, 96, 69, 96, 18, 12, 96, 84, 84, 12, 87, 42, 36]
>>> lm = map(lambda n : (n % 3 == 0), rn)
>>> list(lm)
[False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, True, False, False, True, False, False, True, False, False, False, True, False, True, True, False, False, False, True, False, False, False, True, False, True, True, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, True, False, True, False, True, False, False, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False]
>>> l_div3 = filter(lambda n : (n % 3), rn)
>>> list(l_div3)
[70, 17, 79, 89, 64, 91, 65, 35, 29, 35, 44, 70, 88, 28, 80, 98, 70, 80, 47, 23, 91, 91, 98, 44, 40, 40, 56, 79, 62, 67, 74, 10, 10, 82, 91, 52, 35, 23, 71, 7, 67, 67, 47, 2, 64, 70, 38, 32, 43, 25, 82, 91, 52, 26, 82, 35, 98, 89, 53, 17, 5, 55, 22, 13, 62, 85, 13, 17, 2, 98, 97, 7, 5, 47]
>>> l_div3 = filter(lambda n : (n * 3), rn)
>>> list(l_div3)
[70, 17, 79, 89, 64, 91, 65, 35, 96, 29, 35, 44, 70, 88, 28, 80, 98, 70, 18, 80, 57, 47, 23, 91, 78, 91, 98, 44, 40, 6, 40, 56, 99, 79, 62, 30, 67, 74, 10, 90, 10, 51, 90, 82, 91, 52, 81, 35, 23, 71, 30, 7, 24, 9, 67, 67, 96, 47, 69, 2, 64, 70, 38, 32, 43, 25, 82, 91, 52, 26, 96, 82, 18, 12, 96, 35, 84, 98, 84, 89, 53, 17, 5, 12, 87, 55, 22, 13, 62, 85, 42, 13, 17, 36, 2, 98, 97, 7, 5, 47]
>>> l_div3 = filter(lambda n : not (n % 3), rn)
>>> list(l_div3)
[96, 18, 57, 78, 6, 99, 30, 90, 51, 90, 81, 30, 24, 9, 96, 69, 96, 18, 12, 96, 84, 84, 12, 87, 42, 36]
>>> 
>>> 
>>> 
>>> for i in range(100):
	rn.append(random.randint(10, 99))

	
>>> rn
[70, 17, 79, 89, 64, 91, 65, 35, 96, 29, 35, 44, 70, 88, 28, 80, 98, 70, 18, 80, 57, 47, 23, 91, 78, 91, 98, 44, 40, 6, 40, 56, 99, 79, 62, 30, 67, 74, 10, 90, 10, 51, 90, 82, 91, 52, 81, 35, 23, 71, 30, 7, 24, 9, 67, 67, 96, 47, 69, 2, 64, 70, 38, 32, 43, 25, 82, 91, 52, 26, 96, 82, 18, 12, 96, 35, 84, 98, 84, 89, 53, 17, 5, 12, 87, 55, 22, 13, 62, 85, 42, 13, 17, 36, 2, 98, 97, 7, 5, 47, 44, 20, 33, 11, 11, 91, 33, 50, 83, 79, 26, 53, 78, 90, 13, 54, 33, 44, 86, 53, 41, 27, 73, 79, 34, 19, 55, 36, 85, 76, 94, 68, 17, 23, 56, 44, 40, 41, 23, 78, 54, 43, 86, 40, 71, 63, 90, 88, 92, 65, 50, 68, 32, 27, 50, 59, 23, 25, 61, 54, 41, 32, 44, 28, 40, 92, 23, 56, 13, 42, 89, 76, 31, 26, 24, 64, 69, 21, 11, 34, 96, 79, 18, 59, 16, 64, 73, 31, 14, 11, 68, 55, 52, 74, 72, 57, 99, 50, 69, 89]
>>> del rn
>>> for i in range(100):
	rn.append(random.randint(10, 99))

	
Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    rn.append(random.randint(10, 99))
NameError: name 'rn' is not defined
>>> rn = []
>>> for i in range(100):
	rn.append(random.randint(10, 99))

	
>>> rn
[53, 51, 55, 67, 94, 75, 19, 41, 79, 99, 70, 40, 63, 89, 31, 11, 30, 97, 73, 57, 20, 52, 92, 91, 62, 37, 20, 56, 67, 53, 27, 12, 84, 79, 77, 22, 79, 10, 36, 77, 96, 68, 87, 87, 56, 70, 76, 82, 51, 14, 50, 65, 41, 83, 14, 58, 83, 21, 78, 73, 79, 77, 69, 57, 60, 41, 81, 16, 17, 58, 44, 90, 31, 80, 87, 34, 54, 55, 89, 31, 13, 62, 72, 12, 45, 78, 23, 94, 61, 12, 26, 51, 30, 41, 69, 76, 47, 56, 94, 60]
>>> rn[0]
53
>>> str(rn[0])
'53'
>>> str(rn[0])[1] + str(rn[0])[0]
'35'
>>> str(rn[0])[1]
'3'
>>> str(rn[0])[0]
'5'
>>> int(str(rn[0])[1]) + int(str(rn[0])[0])
8
>>> f = lambda n : int(str(n)[1]) + int(str(n)[0])
>>> f(98)
17
>>> fil = filter(f, rn)
>>> fil
<filter object at 0x0000022D99128CC0>
>>> list(fil)
[53, 51, 55, 67, 94, 75, 19, 41, 79, 99, 70, 40, 63, 89, 31, 11, 30, 97, 73, 57, 20, 52, 92, 91, 62, 37, 20, 56, 67, 53, 27, 12, 84, 79, 77, 22, 79, 10, 36, 77, 96, 68, 87, 87, 56, 70, 76, 82, 51, 14, 50, 65, 41, 83, 14, 58, 83, 21, 78, 73, 79, 77, 69, 57, 60, 41, 81, 16, 17, 58, 44, 90, 31, 80, 87, 34, 54, 55, 89, 31, 13, 62, 72, 12, 45, 78, 23, 94, 61, 12, 26, 51, 30, 41, 69, 76, 47, 56, 94, 60]
>>> f = lambda n : (int(str(n)[1]) + int(str(n)[0])) == 10
>>> f(73)
True
>>> fil = filter(f, rn)
>>> fil
<filter object at 0x0000022D990921D0>
>>> list(fil)
[55, 19, 73, 91, 37, 82, 73, 55]
>>> set(fil)
set()
>>> fil1 = list(fil)
>>> fil1
[]
>>> fil = filter(f, rn)
>>> set(fil)
{37, 73, 82, 19, 55, 91}
>>> ###########################################################
>>> 
>>> fil = filter(f, rn
	     )
>>> list(fil)
[55, 19, 73, 91, 37, 82, 73, 55]
>>> fil = filter(f, rn)
>>> set(fil)
{37, 73, 82, 19, 55, 91}
>>> {37, 73, 82, 19, 55, 91}
{37, 73, 82, 19, 55, 91}

>>> 
>>> 
>>> a = None
>>> ############################################################
>>> from functools import reduce
>>> n = reduce(lambda x,y : x*y, [1,2,3,4])
>>> n
24
>>> f = lambda a,b: a if (a > b) else b

>>> reduce(f, [47,11,42,102,13])
102
>>> ###############################################################
>>> T = ('Naresh', 'Suresh', 'Mahesh')
>>> A = ('India', 'USA', 'UK')
>>> zip(T, A)
<zip object at 0x0000022D99130DC8>
>>> list(zip(T, A))
[('Naresh', 'India'), ('Suresh', 'USA'), ('Mahesh', 'UK')]
>>> z = zip(T, A)
>>> tuple(z)
(('Naresh', 'India'), ('Suresh', 'USA'), ('Mahesh', 'UK'))
>>> dict(z)
{}
>>> z
<zip object at 0x0000022D99132388>
>>> z = zip(T, A)
>>> dict(z)
{'Naresh': 'India', 'Suresh': 'USA', 'Mahesh': 'UK'}
>>> z = zip(T, A)
>>> z2 = zip(*z)
>>> z2
<zip object at 0x0000022D99130DC8>
>>> list(z2)
[('Naresh', 'Suresh', 'Mahesh'), ('India', 'USA', 'UK')]
>>> D = {'Naresh': 'India', 'Suresh': 'USA', 'Mahesh': 'UK'}
>>> ################################################################
>>> def create_generator(N):
	L = range(N+1)
	for i in L:
		yield i*i

>>> gen  = create_generator(10)
>>> type(gen)
<class 'generator'>
>>> for i in gen:
	print(i)

	
0
1
4
9
16
25
36
49
64
81
100
>>> def genfun():
	yield 1
	yield 2yield 3
	
SyntaxError: invalid syntax
>>> def genfun():
	yield 1
	yield 2yield 3
	
SyntaxError: invalid syntax
>>> def genfun():
	yield 1
	yield 2
	yield 3

	
>>> genfun()
<generator object genfun at 0x0000022D9914E7C8>
>>> def retfun():
	return True

>>> retfun()
True
>>> type(retfun)
<class 'function'>
>>> type(genfun)
<class 'function'>
>>> genfun()
<generator object genfun at 0x0000022D9914E7C8>
>>> retfun()
True
>>> for val in genfun():
	print(val)

	
1
2
3
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/generator_yield.py 
1
4
9
16
25
36
49
64
81
100
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/generator_yield.py 
1
4
9
16
25
36
49
64
81
100
1
4
9
16
25
36
49
64
81
100
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/generator_yield.py 
Run 1
1
4
9
16
25
36
49
64
81
100
Run 2
1
4
9
16
25
36
49
64
81
100
>>> 
