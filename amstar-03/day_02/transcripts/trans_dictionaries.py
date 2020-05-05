Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARY
>>> 
>>> s = {'Anil', 35, 'India', 'Oracle'}
>>> s
{35, 'Oracle', 'India', 'Anil'}
>>> L = ['Anil', 35, 'India', 'Oracle']
>>> L
['Anil', 35, 'India', 'Oracle']
>>> T = ('Anil', 35, 'India', 'Oracle')
>>> 
>>> L.insert(2, '15-07-1999')
>>> L
['Anil', 35, '15-07-1999', 'India', 'Oracle']
>>> 
>>> 
>>> D = {'name':'Anil', 'age':35, 'country':'India', 'company':'Oracle'}
>>> type(D)
<class 'dict'>
>>> D['name']
'Anil'
>>> D['age']
35
>>> L['dob'] = '15-07-1999'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    L['dob'] = '15-07-1999'
TypeError: list indices must be integers or slices, not str
>>> D['dob'] = '15-07-1999'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '15-07-1999'}
>>> 
>>> 
>>> 
>>> D2 = {'nplace':'mysore', 'nlanguage':['hindi', 'kannada', 'english', 'tamil']}
>>> d1
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d1
NameError: name 'd1' is not defined
>>> D1
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    D1
NameError: name 'D1' is not defined
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '15-07-1999'}
>>> D2
{'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}
>>> D + D2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    D + D2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> D.update(D1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    D.update(D1)
NameError: name 'D1' is not defined
>>> D.update(D2)
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '15-07-1999', 'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '15-07-1999', 'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}
>>> D = {'name':'Anil', 'age':35, 'country':'India', 'company':'Oracle'}
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> D['native
  
SyntaxError: EOL while scanning string literal
>>> ]
SyntaxError: invalid syntax
>>> D['native']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    D['native']
KeyError: 'native'
>>> D['native'] = 'mysore'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'native': 'mysore'}
>>> D.setdefault('language','English')
'English'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'native': 'mysore', 'language': 'English'}
>>> D.pop('language')
'English'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'native': 'mysore'}
>>> D2
{'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}
>>> D['native']
'mysore'
>>> D['native'] = D2
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'native': {'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}}
>>> D['native']['nlanguage'][1]
'kannada'
>>> 
>>> 
>>> 
>>> 
>>> D.values()
dict_values(['Anil', 35, 'India', 'Oracle', {'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']}])
>>> D.keys()
dict_keys(['name', 'age', 'country', 'company', 'native'])
>>> D.items()
dict_items([('name', 'Anil'), ('age', 35), ('country', 'India'), ('company', 'Oracle'), ('native', {'nplace': 'mysore', 'nlanguage': ['hindi', 'kannada', 'english', 'tamil']})])
>>> 
