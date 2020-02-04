Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # WE will discuss about numbers now
>>> a = 10
>>> a
10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> b = 10.5
>>> type(b)
<class 'float'>
>>> c = 22/7
>>> c
3.142857142857143
>>> type(c)
<class 'float'>
>>> s = 'python'
>>> s.capitalize()
'Python'
>>> a
10
>>> b
10.5
>>> b = 6
>>> b
6
>>> ##########################################
>>> a
10
>>> b
6
>>> # Operators
>>> # Arithmetic
>>> a + b
16
>>> a - b
4
>>> a * b
60
>>> a / b
1.6666666666666667
>>> a % b
4
>>> a // b
1
>>> a ** 2
100
>>> a ** 3
1000
>>> a ** 0.5
3.1622776601683795
>>> a+b = a=a+b
SyntaxError: can't assign to operator
>>> a
10
>>> b
6
>>> a + b
16
>>> a
10
>>> b
6
>>> a = a + b
>>> a
16
>>> # Relational operators
>>> a
16
>>> b
6
>>> a > b
True
>>> a < b
False
>>> a == b
False
>>> a == b + 10
True
>>> a != 10 * 3
True
>>> a >= b
True
>>> a <= b
False
>>> # Logical operators
>>> a > b and b < 30
True
>>> a < b and a == 10 + 6
False
>>> a < b or a == 10 + 6
True
>>> not (a < b) and a == 10 + 6
True
>>> ##############################################
>>> a
16
>>> a = 100
>>> a
100
>>> type(a)
<class 'int'>
>>> a = 10
>>> a = 100
>>> a + 10
110
>>> a - 10
90
>>> a
100
>>> bin(a)
'0b1100100'
>>> x = bin(a)
>>> type(a)
<class 'int'>
>>> type(x)
<class 'str'>
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> x
'0b1100100'
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '0b1100100'
>>> int('456')
456
>>> int(x, 2)
100
>>> abs(10.4)
10.4
>>> abs(-23.4565477)
23.4565477
>>> int('0o144',2)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int('0o144',2)
ValueError: invalid literal for int() with base 2: '0o144'
>>> int('0o144',8)
100
>>> ##########################################################
>>> # Built in modules for numbers in python
>>> a = 100
>>> b = 80
>>> gcd(a, b)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    gcd(a, b)
NameError: name 'gcd' is not defined
>>> import math
>>> math.gcd(a, b)
20
>>> math.sqrt(144)
12.0
>>> math.factorial(5)
120
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * (3.1416/180))
0.9999999999932537
>>> math.sin(90 * ((22/7)/180))
0.9999998001333682
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
68
>>> random.randint(1, 100)
42
>>> random.randint(1, 100)
50
>>> random.randint(1, 100)
60
>>> random.randint(1, 100)
13
>>> random.randint(1, 100)
28
>>> #######################################################
>>> # How to take user input
>>> input("Enter a number: ")
Enter a number: 56
'56'
>>> uin = input('Enter a number:')
Enter a number:23
>>> uin
'23'
>>> type(uin)
<class 'str'>
>>> uin + 10
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    uin + 10
TypeError: can only concatenate str (not "int") to str
>>> int(uin) + 10
33
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/Oracle Py 01/sum_of_numbers.py 
Enter a number: 45
Enter another number: 65
The sum is:  4565
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/Oracle Py 01/sum_of_numbers.py 
Enter a number: 12
Enter another number: 23
The sum is:  35
>>> 
