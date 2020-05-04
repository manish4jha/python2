Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers
>>> a = 5
>>> b = 2
>>> type(a)
<class 'int'>
>>> c = 22/7
>>> type(c)
<class 'float'>
>>> # -------------------- OPERATORS
>>> # ARITHMETIC OPERATORS
>>> a + b
7
>>> print('SUM :', a + b)
SUM : 7
>>> s = a + b
>>> s
7
>>> print('SUM :', s)
SUM : 7
>>> a + b
7
>>> print('SUM :', 's')
SUM : s
>>> print('SUM :', s)
SUM : 7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> print('SUM :' s)
SyntaxError: invalid syntax
>>> print('SUM :', s)
SUM : 7
>>> a % b
1
>>> a // b
2
>>> a ** 2
25
>>> # Conditional Operators
>>> a
5
>>> b
2
>>> a > b  # is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a != b
True
>>> a == (b * 2 + 1)
True
>>> #  Logical Operators
>>> # and or not
>>> a > b and b < 10
True
>>> a > b and b > 10
False
>>> a > b or a + b == 6
True
>>> a > b
True
>>> not a > b
False
>>> # ------------------- Functions
>>> 
>>> a  = 100
>>> type(a)
<class 'int'>
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> type(a)
<class 'int'>
>>> x = hex(a)
>>> type(x)
<class 'str'>
>>> int(100)
100
>>> float(a)
100.0
>>> f = float(a)
>>> type(f)
<class 'float'>
>>> str(a)
'100'
>>> s = str(a)
>>> type(s)
<class 'str'>
>>> i = '100'
>>> type(i)
<class 'str'>
>>> i + 10
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    i + 10
TypeError: can only concatenate str (not "int") to str
>>> int(i) + 10
110
>>> i = '123A'
>>> int(i)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(i)
ValueError: invalid literal for int() with base 10: '123A'
>>> j = '1101001'
>>> int(j)
1101001
>>> int(j, 2)
105
>>> bin(105)
'0b1101001'
>>> i
'123A'
>>> int(i, 16)
4666
>>> hex(4666)
'0x123a'
>>> a = 5
>>> b = 2
>>> a - b
3
>>> b - a
-3
>>> abs(a - b)
3
>>> abs(b - a)
3
>>> # ------------------------ modules
>>> factorial(5)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    factorial(5)
NameError: name 'factorial' is not defined
>>> import math
>>> math.factorial(5)
120
>>> math.gcd(36, 72)
36
>>> math.sqrt(100)
10.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * (22/7)/180)
0.9999998001333682
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
89
>>> random.randint(1, 100)
60
>>> random.randint(1, 100)
29
>>> random.randint(1, 100)
94
>>> random.randint(1, 100)
83
>>> random.randint(1, 100)
52
>>> random.randint(1, 100)
45
>>> random.randint(1, 100)
68
>>> 
