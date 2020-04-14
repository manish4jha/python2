Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings: immutability
>>> s = 'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> s = 'jython'
>>> s
'jython'
>>> # Acessability
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[10]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[10]
IndexError: string index out of range
>>> hcq = 'hydroxychloroquine'
>>> len(hcq)
18
>>> hcq(17)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    hcq(17)
TypeError: 'str' object is not callable
>>> hcq[17]
'e'
>>> hcq[-1]
'e'
>>> s
'python'
>>> s[1:3]
'yt'
>>> s[1:4]
'yth'
>>> s[3:5]
'ho'
>>> s[3:6]
'hon'
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[3:]
'hon'
>>> s[-1]
'n'
>>> s[-3: -1]
'ho'
>>> s[-3:]
'hon'
>>> s[:]
'python'
>>> s[1:5:2]
'yh'
>>> # ytho -> yh
>>> s[::2]
'pto'
>>> # python -> pto
>>> s[::3]
'ph'
>>> # python -> ph
>>> s[1:5:1]
'ytho'
>>> s[-5:-1]
'ytho'
>>> s[-1:-5]
''
>>> s[::-1]
'nohtyp'
>>> s[1:5:-1]
''
>>> s[-5:-1:-1]
''
>>> s1 = s[1:5]
>>> s1[::-1]
'ohty'
>>> s2 = s[-5:-1]
>>> s2
'ytho'
>>> s2[::-1]
'ohty'
>>> #######################################################
>>> # Operators
>>> s1 = 'py'
>>> s2 = 'thon'
>>> s3 = "python"
>>> s4 = '''This
is
a
multiline
string
'''
>>> type(s1)
<class 'str'>
>>> type(s4)
<class 'str'>
>>> print(s1 + s2)
python
>>> print(s4)
This
is
a
multiline
string

>>> 10 + 20
30
>>> 'py' + 'thon'
'python'
>>> 10 + 'py'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    10 + 'py'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(10) + 'py'
'10py'
>>> 10 + int('py')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    10 + int('py')
ValueError: invalid literal for int() with base 10: 'py'
>>> i = '1234'
>>> type(i)
<class 'str'>
>>> int(i)
1234
>>> float(i)
1234.0
>>> j = 'abcd234'
>>> int(i)
1234
>>> int(j)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(j)
ValueError: invalid literal for int() with base 10: 'abcd234'
>>> k = '12.345'
>>> float(k)
12.345
>>> k + 10
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    k + 10
TypeError: can only concatenate str (not "int") to str
>>> int(k) + 10
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(k) + 10
ValueError: invalid literal for int() with base 10: '12.345'
>>> float(k) + 10
22.345
>>> i
'1234'
>>> i * 3
'123412341234'
>>> s
'python'
>>> len(s)
6
>>> 'th' in s
True
>>> 'app' in s
False
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> k
'12.345'
>>> type(k)
<class 'str'>
>>> int(k)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    int(k)
ValueError: invalid literal for int() with base 10: '12.345'
>>> float(k)
12.345
>>> ##################################### IN-built functions to process strings
>>> # case, check, modify, search
>>> k
'12.345'
>>> s
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'python'
>>> # Case
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> # checking
>>> s1 = '1234'
>>> s2 = 'abc56'
>>> s3 = ' '
>>> s4 = '*&^*&'
>>> s
'python'
>>> s.isupper()
False
>>> s.islower()
True
>>> s5 = 'PyhtoN'
>>> s5.isupper()
False
>>> s5.islower()
False
>>> s5.lower().isupper()
False
>>> s5.lower().islower()
True
>>> s5
'PyhtoN'
>>> s5.lower()
'pyhton'
>>> s5
'PyhtoN'
>>> s6 = s5.lower()
>>> s5
'PyhtoN'
>>> s6
'pyhton'
>>> s1
'1234'
>>> s1.isdigit()
True
>>> s2
'abc56'
>>> s2.isdigit()
False
>>> int(s2)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    int(s2)
ValueError: invalid literal for int() with base 10: 'abc56'
>>> if s2.isdigit():
	print(int(s2))

	
>>> if s2.isalnum():
	print(s2)

	
abc56
>>> if s2.isalpha():
	print(s2)

	
>>> s4
'*&^*&'
>>> s4.isdigit()
False
>>> s4.isalnum()
False
>>> s4.isalpha()
False
>>> s3
' '
>>> s3.isspace()
True
>>> site = 'www.google.com'
>>> type(site)
<class 'str'>
>>> site.startswith('https')
False
>>> site.endswith('com')
True
>>> # SEARCH
>>> s
'python'
>>> 'th' in s
True
>>> s.find('th')
2
>>> # modify
>>> ip = '192-168-1-1'
>>> ip.replace('-', '.')
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> newip = ip.replace('-', '.')
>>> newip
'192.168.1.1'
>>> text = 'Searches the string for a specified value and returns the position of where it was found'
>>> s1 = 'Searches'
>>> s1.replace('e', 'l')
'Slarchls'
>>> s1
'Searches'
>>> s1 = s1.replace('e', 'l')
>>> s1
'Slarchls'
>>> s1 = 'Searches'
>>> s1
'Searches'
>>> s1.replace('e', 'l')
'Slarchls'
>>> s1
'Searches'
>>> s12 = s1.replace('e', 'l')
>>> s1
'Searches'
>>> s12
'Slarchls'
>>> text
'Searches the string for a specified value and returns the position of where it was found'
>>> type(text)
<class 'str'>
>>> L = text.split()
>>> L
['Searches', 'the', 'string', 'for', 'a', 'specified', 'value', 'and', 'returns', 'the', 'position', 'of', 'where', 'it', 'was', 'found']
>>> type(L)
<class 'list'>
>>> L1 = text.split('r')
>>> L1
['Sea', 'ches the st', 'ing fo', ' a specified value and ', 'etu', 'ns the position of whe', 'e it was found']
>>> L
['Searches', 'the', 'string', 'for', 'a', 'specified', 'value', 'and', 'returns', 'the', 'position', 'of', 'where', 'it', 'was', 'found']
>>> ' '.join(L)
'Searches the string for a specified value and returns the position of where it was found'
>>> '-'.join(L)
'Searches-the-string-for-a-specified-value-and-returns-the-position-of-where-it-was-found'
>>> 'R'.join(L1)
'SeaRches the stRing foR a specified value and RetuRns the position of wheRe it was found'
>>> L3 = 'R'.join(L1)
>>> L3.count('R')
6
>>> L3.count('s')
6
>>> s = '    python perl   '
>>> s
'    python perl   '
>>> len(s)
18
>>> s.startswith('py')
False
>>> s.strip()
'python perl'
>>> s.lstrip()
'python perl   '
>>> s.rstrip()
'    python perl'
>>> # Misc # Assignment
>>> # Study and demonstrate the use of translate and maketrans functions
>>> # under string operation in python
