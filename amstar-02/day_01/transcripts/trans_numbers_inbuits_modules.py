Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = 5
>>> b = 2
>>> b - a
-3
>>> a - b
3
>>> abs(b - a)
3
>>> a = 100
>>> type(a)
<class 'int'>
>>> b = float(a)
>>> b
100.0
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> a.bit_length()
7
>>> str(100)
'100'
>>> ####################### Modules
>>> sqrt(144)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sqrt(144)
NameError: name 'sqrt' is not defined
>>> import math
>>> math.sqrt(144)
12.0
>>> math.gcd(15, 18)
3
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
36
>>> random.randint(1, 100)
91
>>> random.randint(1, 100)
98
>>> random.randint(1, 100)
7
>>> random.randint(1, 100)
28
>>> random.randint(1, 100)
94
>>> random.randint(1, 100)
50
>>> random.randint(1, 100)
3
>>> random.randomm()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    random.randomm()
AttributeError: module 'random' has no attribute 'randomm'
>>> random.random()
0.07893549897753982
>>> random.random()random.random()
SyntaxError: invalid syntax
>>> random.random()random.random()
>>> random.random()
0.0498301446889009
>>> random.random()
0.9494272282063324
>>> random.random()
0.1876340186290838
>>> random.random()
0.19075332074009688
>>> random.random()
0.7901223121474554
>>> 
