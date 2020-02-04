Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = {'Anil', 35, 'India'}
>>> s
{'Anil', 35, 'India'}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> L = ['Anil', 35, 'India']
>>> L[0]
'Anil'
>>> L[1]
35
>>> L[2]
'India'
>>> # L[2] ---> Country
>>> L.insert(-2, '13-5-99')
>>> L
['Anil', '13-5-99', 35, 'India']
>>> L[2]
35
>>> D = {'name':'Anil', 'age':35, 'country':'India'}
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['country']
'India'
>>> D['dob'] = '13-5-99'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99'}
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['country']
'India'
>>> D['dob']
'13-5-99'
>>> ###################################################################
>>> D = {'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99'}
>>> D['name']
'Anil'
>>> D['job']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    D['job']
KeyError: 'job'
>>> D['job'] = 'engineer'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer'}
>>> D.setdefault('salary')
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer', 'salary': None}
>>> D['salary'] = '100000 USD'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer', 'salary': '100000 USD'}
>>> D.setdefault('hobbies', ['music', 'hiking'])
['music', 'hiking']
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer', 'salary': '100000 USD', 'hobbies': ['music', 'hiking']}
>>> D1 = { 'company':'oracle', 'dept':'finance'}
>>> D.update(D1)
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer', 'salary': '100000 USD', 'hobbies': ['music', 'hiking'], 'company': 'oracle', 'dept': 'finance'}
>>> D.pop('dept')
'finance'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'dob': '13-5-99', 'job': 'engineer', 'salary': '100000 USD', 'hobbies': ['music', 'hiking'], 'company': 'oracle'}
>>> D.sort()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    D.sort()
AttributeError: 'dict' object has no attribute 'sort'
>>> reversed(D)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    reversed(D)
TypeError: 'dict' object is not reversible
>>> ############################################################################
>>> D.keys()
dict_keys(['name', 'age', 'country', 'dob', 'job', 'salary', 'hobbies', 'company'])
>>> sorted(D.keys())
['age', 'company', 'country', 'dob', 'hobbies', 'job', 'name', 'salary']
>>> D.values()
dict_values(['Anil', 35, 'India', '13-5-99', 'engineer', '100000 USD', ['music', 'hiking'], 'oracle'])
>>> D.items()
dict_items([('name', 'Anil'), ('age', 35), ('country', 'India'), ('dob', '13-5-99'), ('job', 'engineer'), ('salary', '100000 USD'), ('hobbies', ['music', 'hiking']), ('company', 'oracle')])
>>> 
#################
>>> 
>>> 
>>> D1 = {'Name': 'Mark', 'EID': 123456, 'Country': 'India', ('Name', 'Country'): ['Anil', 'India']}
>>> D1
{'Name': 'Mark', 'EID': 123456, 'Country': 'India', ('Name', 'Country'): ['Anil', 'India']}
>>> D.keys()
dict_keys(['name', 'age', 'country', 'dob', 'job', 'salary', 'hobbies', 'company'])
>>> D1.keys()
dict_keys(['Name', 'EID', 'Country', ('Name', 'Country')])
>>> sorted(D1.keys())
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sorted(D1.keys())
TypeError: '<' not supported between instances of 'tuple' and 'str'
>>> D2 = {1:'a', 2:'b'}
>>> D2
{1: 'a', 2: 'b'}
>>> sorted(D2.keys())
[1, 2]
>>> D1[('Name', 'Country')]
['Anil', 'India']
>>> 
