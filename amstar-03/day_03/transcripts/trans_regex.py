Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = 'Ratatouille'

>>> string[4:6]
'to'
>>> string[4:7]
'tou'
>>> string = 'if stu chews shoes, should stu choose the shoes he chews'

>>> for i in (re.finditer(r'\b[a-z]ho\w*', string)):
	print (i.group(), i.span()))
	
SyntaxError: invalid syntax
>>> x = re.finditer(r'\b[a-z]ho\w*', string)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = re.finditer(r'\b[a-z]ho\w*', string)
NameError: name 're' is not defined
>>> import re
>>> x = re.finditer(r'\b[a-z]ho\w*', string)
>>> type(x)
<class 'callable_iterator'>
>>> x = re.finditer(r'\b[a-z]ho\w*', string)
>>> for obj in x:
	print(obj)

	
<re.Match object; span=(13, 18), match='shoes'>
<re.Match object; span=(20, 26), match='should'>
<re.Match object; span=(31, 37), match='choose'>
<re.Match object; span=(42, 47), match='shoes'>
>>> x = re.finditer(r'\b[a-z]ho\w*', string)
>>> for obj in x:
	print(x.group(), x.span())

	
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(x.group(), x.span())
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> x = re.finditer(r'\b[a-z]ho\w*', string)
>>> for obj in x:
	print(obj.group(), obj.span())

	
shoes (13, 18)
should (20, 26)
choose (31, 37)
shoes (42, 47)
>>> string[13:18]
'shoes'
>>> string[20:26]
'should'
>>> string[31:37]
'choose'
>>> string[42:47]
'shoes'
>>> x = re.findall(r'\b[a-z]ho\w*', string)
>>> for obj in x:
	print(obj)

	
shoes
should
choose
shoes
>>> type(x)
<class 'list'>
>>> for obj in x:
	print(obj.span(), obj.group())

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print(obj.span(), obj.group())
AttributeError: 'str' object has no attribute 'span'
>>> # --------------------------- Senthil Kumar ---------- #
>>> 
>>> 
>>> 
>>> email = "tony@tiremove_thisger.net"

>>> # tony@tiger.net
>>> email[:6]
'tony@t'
>>> email[:7]
'tony@ti'
>>> email[-7:]
'ger.net'
>>> email[:7] + email[-7:]
'tony@tiger.net'
>>> 
>>> import re
>>> m = re.search('remove_this', email)
>>> m
<re.Match object; span=(7, 18), match='remove_this'>
>>> m.group()
'remove_this'
>>> m.span()
(7, 18)
>>> m.start()
7
>>> m.end()
18
>>> email[:m.start()] + email[m.end():]
'tony@tiger.net'
>>> 
>>> 
>>> # ---------------------------------------------
>>> 
>>> string = 'This is a floating point value --> 12.345'
>>> m = re.search(r"\d+\.\d+", string)
>>> m
<re.Match object; span=(35, 41), match='12.345'>
>>> m.group()
'12.345'
>>> m.span()
(35, 41)
>>> string[35:41]
'12.345'
>>> m = re.search(r"(\d+)\.(\d+)", string)
>>> m.group()
'12.345'
>>> m.group(1)
'12'
>>> m.group(2)
'345'
>>> m.groups()
('12', '345')
>>> t = m.groups()
>>> t[0]
'12'
>>> t[1]
'345'
>>> m = re.search(r"(\d+)\.(\d+)", string)
>>> s = r"(\d+)\.(\d+)"
>>> type(s)
<class 'str'>
>>> s.upper()
'(\\D+)\\.(\\D+)'
>>> m.groupdict()
{}
>>> m
<re.Match object; span=(35, 41), match='12.345'>
>>> m = re.search(r"(?P<integer>\d+)\.(?P<decimal>\d+)", string)
>>> m.groups()
('12', '345')
>>> m.groupdict()
{'integer': '12', 'decimal': '345'}
>>> d =  m.groupdict()
>>> d['decimal']
'345'
>>> d['integer']
'12'
>>> 
>>> 
>>> # ---------------------------------------------------
>>> 
>>> email = "Rajesh +913456775563 raj@oracle.com"
>>> pattern = "(\w+)@(\w+)"
>>> m = re.search(pattern, email)
>>> m.group()
'raj@oracle'
>>> m.span()
(21, 31)
>>> pattern = "(\w+)@(\w+\.\w+)"
>>> m = re.search(pattern, email)
>>> m.group()
'raj@oracle.com'
>>> m.span()
(21, 35)
>>> m.groups()
('raj', 'oracle.com')
>>> m.groups()[0]
'raj'
>>> m.group(1)
'raj'
>>> # d = { 'user':'raj', 'domain':'oracle.com' }
>>> pattern = "(?P<user>\w+)@(?P<domain>\w+\.\w+)"
>>> m = re.search(pattern, email)
>>> d = m.groupdict()
>>> d
{'user': 'raj', 'domain': 'oracle.com'}
>>> 
>>> 
>>> # ---------------------------------------------
>>> 
>>> 
>>> 
>>>  email = "tony@tiremove_thisger.net"
 
SyntaxError: unexpected indent
>>> 
>>>  email = "tony@tiremove_thisger.net"
 
SyntaxError: unexpected indent
>>> email = "tony@tiremove_thisger.net"
>>> pattern = "r\w+\_\w+r"
>>> m = re.search(pattern, email)
>>> m.group()
'remove_thisger'
>>> pattern = "r\w+\_\w+?r"
>>> m = re.search(pattern, email)
>>> m.group()
'remove_thisger'
>>> pattern = "r\w+\_.*?r"
>>> m = re.search(pattern, email)
>>> m.group()
'remove_thisger'
>>> pattern = "r\w+\_.*?s"
>>> m = re.search(pattern, email)
>>> m.group()
'remove_this'
>>> m.start()
7
>>> m.end()
18
>>> email
'tony@tiremove_thisger.net'
>>> new = re.sub(pattern, '', email)
>>> new
'tony@tiger.net'
>>> 
>>> # -------------------------- Anitha Nagraj ------------
>>> 
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a5x matched in 'a5xb'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
a5e matched in 'a5e'
a6f matched in 'a6f'
a6c matched in '123 a6c'
a5b matched in 'a5b'
a55 matched in 'a55b'
a55 matched in 'a555b'
a55 matched in 'a5555b'
a55 matched in 'a55555b'
a55 matched in 'a555555b'
a5x matched in 'a5xb'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a5x matched in 'a5xb'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a5e matched in 'a5e'
a6f matched in 'a6f'
a5b matched in 'a5b'
a5x matched in 'a5xbmnop'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a5e matched in 'a5e'
a6f matched in 'a6f'
a6c matched in '123 a6c'
a5b matched in 'a5b'
a5x matched in 'a5xbmnop'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
3 a6 matched in '123 a6c'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
ama matched in 'amazing'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
bc ab matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
3+2 matched in '3+2=5'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
123 matched in '123 a6c'
55 matched in 'a55b'
555 matched in 'a555b'
5555 matched in 'a5555b'
55555 matched in 'a55555b'
555555 matched in 'a555555b'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
bc matched in 'abc'
a6 matched in 'a6f'
a6 matched in '123 a6c'
bc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
ama matched in 'amazing'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
123 a matched in '123 a6c'
def g matched in 'def ghi'
abc a matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a6 matched in 'a6f'
a6 matched in '123 a6c'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a6 matched in 'a6f'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
a6c matched in '123 a6c'
abc matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
abc matched in 'abc'
a6c matched in '123 a6c'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
ab matched in 'ab'
ab matched in 'abc ab'
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
ab matched in 'abc'
ab matched in 'abc ab'
>>> text = 'This isample a sample'
>>> pattern = "sam"
>>> m = re.findall(pattern, text)
>>> m
['sam', 'sam']
>>> m = re.finditer(pattern, text)
>>> m
<callable_iterator object at 0x000001BF09C977B8>
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(m.group(), m.span())

	
Traceback (most recent call last):
  File "<pyshell#140>", line 2, in <module>
    print(m.group(), m.span())
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
sam (6, 9)
sam (15, 18)
>>> pattern = "\bsam"
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
>>> m = re.findall(pattern, text)
>>> m
[]
>>> pattern = "\ssam"
>>> for obj in m:
	print(obj.group(), obj.span())

	
>>> m = re.findall(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
Traceback (most recent call last):
  File "<pyshell#155>", line 2, in <module>
    print(obj.group(), obj.span())
AttributeError: 'str' object has no attribute 'group'
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
 sam (14, 18)
>>> text = 'This isample a,sample'
>>> pattern = "\bsam"
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
>>> pattern = " sam"
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
>>> text = 'This isample a sample'
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
 sam (14, 18)
>>> 
>>> 
>>> pattern = r"\bsam"
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
sam (15, 18)
>>> "\n\t\b\a\r\f\s"
'\n\t\x08\x07\r\x0c\\s'

>>> print("\nSam")

Sam
>>> print("5\nSam")
5
Sam
>>> print("5\tSam")
5	Sam
>>> print(r"5\nSam")
5\nSam
>>> print(r"5\tSam")
5\tSam
>>> pattern = r"\Bsam"
>>> m = re.finditer(pattern, text)
>>> for obj in m:
	print(obj.group(), obj.span())

	
sam (6, 9)
>>> 
==== RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/code/regex_ex.py ====
a555 matched in 'a555b'
a5555 matched in 'a5555b'
a55555 matched in 'a55555b'
a555555 matched in 'a555555b'
>>> 
