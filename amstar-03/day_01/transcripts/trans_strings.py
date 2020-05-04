Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> # -------- Accessability through sub-scripting
>>> # s[index]
>>> # s[start:end]
>>> # s[start:end:interval]
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[5]
'n'
>>> s[6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[6]
IndexError: string index out of range
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-6]
'p'
>>> s[-7]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[-7]
IndexError: string index out of range
>>> s[1:3]
'yt'
>>> s[2:6]
'thon'
>>> # [1:3] ---> 1, 2   ---> yt
>>> # [2:6] ----> 2, 3, 4, 5  ----> thon
>>> s[-4:-1]
'tho'
>>> # [-4:-1]  ----> -4, -3, -2  ---> tho
>>> s[-1:-4]
''
>>> # [-1:-4] ----> -1, -2, -3  ----> python doesn't read in the reverse order
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[3:6]
'hon'
>>> h[3:]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    h[3:]
NameError: name 'h' is not defined
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> s[1:5]
'ytho'
>>> s[1:5:2]
'yh'
>>> s[1:5:1]
'ytho'
>>> s[::2]
'pto'
>>> s[1::2]
'yhn'
>>> s[::3]
'ph'
>>> s[::-1]
'nohtyp'
>>> # --------------------- immutable nature
>>> s
'python'
>>> s[0]
'p'
>>> s[0] = 'c'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s[0] = 'c'
TypeError: 'str' object does not support item assignment
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> s = 'jython'
>>> s
'jython'
>>> s[0] = 'p'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s[0] = 'p'
TypeError: 'str' object does not support item assignment
>>> # --------------- Operators
>>> 
>>> s1 = 'py'
>>> s2 = 'thon'
>>> s1 + s2
'python'
>>> 'comp' + 'uter'
'computer'
>>> '12' + str(13)
'1213'
>>> 'python' * 3
'pythonpythonpython'
>>> len(s)
6
>>> 'th' in s
True
>>> s
'jython'
>>> 
>>> 'app' in s
False
>>> s1
'py'
>>> s2
'thon'
>>> del s1
>>> del s2
>>> s1
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> s2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> s
'jython'
>>> s = 'python'
>>> # Strings are immutable
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> s
'python'
>>> # --------------------- built-in string functions
>>> 
>>> # Case
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s
'python'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> s
'python'
>>> # Querying
>>> s
'python'
>>> print(s)
python
>>> print(s.upper())
PYTHON
>>> s
'python'
>>> print(s)
python
>>> s1 = s.upper()
>>> s1
'PYTHON'
>>> s
'python'
>>> s1[0] = "J"
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s1[0] = "J"
TypeError: 'str' object does not support item assignment
>>> s
'python'
>>> s
'python'
>>> s = 'Java'
>>> s
'Java'
>>> s1 = s.upper()
>>> s = 'Python'
>>> s[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> s = 'Java'
>>> s
'Java'
>>> s[1]
'a'
>>> s[1] = 'b'
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    s[1] = 'b'
TypeError: 'str' object does not support item assignment
>>> s =
SyntaxError: invalid syntax
>>> s = s.upper()
>>> s
'JAVA'
>>> s
'JAVA'
>>> s = 10
>>> s
10
>>> s = 'python'
>>> s.upper()
'PYTHON'
>>> s
'python'
>>> s = s.upper()
>>> s
'PYTHON'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> # Querying functions
>>> s1 = '1234'
>>> s2 = 'asd345'
>>> s3 = ' '
>>> s4 = '*&^&'
>>> s
'PYTHON'
>>> s.isupper()
True
>>> s.islower()
False
>>> s1.isalpha()
False
>>> s1.isdigit()
True
>>> s2.isalpha()
False
>>> s2.isalnum()
True
>>> s3.isspace()
True
>>> s4.isalnum()
False
>>> s4.isdigit()
False
>>> site = 'www.oracle.com'
>>> type(site)
<class 'str'>
>>> site.startswith('http')
False
>>> site.endswith('com')
True
>>> # Modifications
>>> s = ''
>>> s.isspace()
False
>>> s == None
False
>>> s == ''
True
>>> # Special values in python: True False None
>>> s
''
>>> type(s)
<class 'str'>
>>> s = None
>>> type(s)
<class 'NoneType'>
>>> ip = '191-168-1-1'
>>> type(ip)
<class 'str'>
>>> ip[3]
'-'
>>> ip[3] = '.'
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    ip[3] = '.'
TypeError: 'str' object does not support item assignment
>>> ip.replace('-', '.')
'191.168.1.1'
>>> ip
'191-168-1-1'
>>> newip = ip.replace('-', '.')
>>> newip
'191.168.1.1'
>>> s = '       https://www.abc.com/?a=56   '
>>> s.rstrip()
'       https://www.abc.com/?a=56'
>>> s.lstrip()
'https://www.abc.com/?a=56   '
>>> s.strip()
'https://www.abc.com/?a=56'
>>> s.rjust()
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    s.rjust()
TypeError: rjust() takes at least 1 argument (0 given)
>>> rjust(s)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    rjust(s)
NameError: name 'rjust' is not defined
>>> s = 'python'
>>> s.rjust(20)
'              python'
>>> s
'python'
>>> sr = s.rjust(20)
>>> sr
'              python'
>>> s
'python'
>>> sl = s.ljust(20, '*')
>>> sl
'python**************'
>>> text = 'python is an excellent programming language'
>>> text.split()
['python', 'is', 'an', 'excellent', 'programming', 'language']
>>> text.split('o')
['pyth', 'n is an excellent pr', 'gramming language']
>>> L = ['python', 'is', 'an', 'excellent', 'programming', 'language']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'python-is-an-excellent-programming-language'
>>> text
'python is an excellent programming language'
>>> 
>>> # Search related functions
>>> s
'python'
>>> s.find('o')
4
>>> s = 'mississippi'
>>> s.find('s')
2
>>> s.find('ssi')
2
>>> s.count('s)
	
SyntaxError: EOL while scanning string literal
>>> s.count('s')
4
>>> s.count('ssi')
2
>>> 
