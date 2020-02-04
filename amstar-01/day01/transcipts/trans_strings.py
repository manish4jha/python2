Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> s[2]
't'
>>> s[-4]
't'
>>> s[0]
'p'
>>> s[-1]
'n'
>>> s[1:4]
'yth'
>>> s[2:5]
'tho'
>>> s[2:6]
'thon'
>>> s[2:]
'thon'
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[:]
'python'
>>> s[-5:-2]
'yth'
>>> s[-2:-5]
''
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[1::2]
'yhn'
>>> s[::-1]
'nohtyp'
>>> s[::-2]
'nhy'
>>> ################################################
>>> # Some operators that work on strings
>>> s1 = 'abc'
>>> s2 = 'def'
>>> s1 + s2
'abcdef'
>>> s3 = s1 + s2 # concatenation
>>> s3
'abcdef'
>>> s1 * 3 # replication
'abcabcabc'
>>> len(s3)
6
>>> 'cd' in s3
True
>>> 'app' in s3
False
>>> s1
'abc'
>>> s2
'def'
>>> s3
'abcdef'
>>> del s3
>>> s3
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s3
NameError: name 's3' is not defined
>>> #########################################################
>>> # Functions to work on the case of the string
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> # Question the content in the string
>>> s1 = '324'
>>> s2 = '  '
>>> s3 = '*^*&'
>>> s4 = 'JH76'
>>> s1.isdigit()
True
>>> s2.isdigit()
False
>>> s4.isdigit()
False
>>> s4.isalpha()
False
>>> s4.isalnum()
True
>>> s3.isalnum()
False
>>> s2.isspace()
True
>>> s
'python'
>>> s.islower()
True
>>> s.upper()
'PYTHON'
>>> s.isupper()
False
>>> s
'python'
>>> #####################################
>>> s5 = 'that's it'
SyntaxError: invalid syntax
>>> s5 = 'that\'s it'
>>> print(s5)
that's it
>>> ########################################
>>> # Searching
>>> s
'python'
>>> 'p' in s
True
>>> s.index('p')
0
>>> s.find('p')
0
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.find('z')
-1
>>> s6 = 'mississippi'
>>> s6.count('s')
4
>>>  s5='\\''
 
SyntaxError: unexpected indent
>>> s5='\\''
SyntaxError: EOL while scanning string literal
>>> s5='\\\''
>>> print(s5)
\'
>>> s6.count('ss')
2
>>> ########################################
>>> # Modifications
>>> ip = '192:89:23:43'
>>> ip[3]
':'
>>> ip[3] = '.'
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    ip[3] = '.'
TypeError: 'str' object does not support item assignment
>>> ip.replace(':', '.')
'192.89.23.43'
>>> ip
'192:89:23:43'
>>> ip2 = ip.replace(':', '.')
>>> ip2
'192.89.23.43'
>>> text = '   python  '
>>> text.lstrip()
'python  '
>>> text.rstrip()
'   python'
>>> text.strip()
'python'
>>> site = 'www.google.com'
>>> site.startswith('www')
True
>>> site.endswith('com')
True
>>> site.endswith('org')
False
>>> text = 'This is a course on python'
>>> text.split()
['This', 'is', 'a', 'course', 'on', 'python']
>>> text.split('s')
['Thi', ' i', ' a cour', 'e on python']
>>> L = text.split()
>>> L
['This', 'is', 'a', 'course', 'on', 'python']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'This-is-a-course-on-python'
>>> ####################################################
>>> 
>>> L
['This', 'is', 'a', 'course', 'on', 'python']
>>> L[0]
'This'
>>> L[1]
'is'
>>> L[2]
'a'
>>> 
