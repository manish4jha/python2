Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 'Anil', 35, 'India', 'Oracle'
>>> L = ['Anil', 35, 'India', 'Oracle']
>>> S = {'Anil', 35, 'India', 'Oracle'}
>>> T = ('Anil', 35, 'India', 'Oracle')
>>> 
>>> type(L)
<class 'list'>
>>> type(S)
<class 'set'>
>>> type(T)
<class 'tuple'>
>>> L[1]
35
>>> T[1]
35
>>> S
{'Anil', 'India', 35, 'Oracle'}
>>> L = ['Anil', 35, 'India', 'Oracle']
>>> L.insert(2, '300000$')
>>> L
['Anil', 35, '300000$', 'India', 'Oracle']
>>> D = { 'name' : 'Anil', 'age' : 35, 'country': 'India', 'company' : 'Oracle' }
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['country']
'India'
>>> D['company']
'Oracle'
>>> D['salary'] = '300000$'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}
>>> # ---------------------------------------------------
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}
>>> len(D)
5
>>> D1 = {'tax': '10', 'location':'Bangalore' }
>>> D + D1
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    D + D1
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> D.update(D1)
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore'}
>>> D['ranking']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    D['ranking']
KeyError: 'ranking'
>>> D['ranking'] = 5
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5}
>>> D.setdefault('addr', {'street' : '23rd croos', 'district':'mysore', 'state':'karnataka'})
{'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}}
>>> D['addr']['state']
'karnataka'
>>> # D['ranking'] = 5  ==>>> D.setdefault('ranking', 5)
>>> D['sname']
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    D['sname']
KeyError: 'sname'
>>> D.setdefault('sname')
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}, 'sname': None}
>>> {'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}, 'sname': None}
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}, 'sname': None}

>>> 
>>> 
>>> D['sname'] = 'kumar'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}, 'sname': 'kumar'}
>>> D['salary'] = '400000$'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '400000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}, 'sname': 'kumar'}
>>> D.pop('sname')
'kumar'
>>> D
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '400000$', 'tax': '10', 'location': 'Bangalore', 'ranking': 5, 'addr': {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}}
>>> 
>>> 
>>> # --------------------------------
>>> 
>>> D.values()
dict_values(['Anil', 35, 'India', 'Oracle', '400000$', '10', 'Bangalore', 5, {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'}])
>>> D.keys()
dict_keys(['name', 'age', 'country', 'company', 'salary', 'tax', 'location', 'ranking', 'addr'])
>>> D.items()
dict_items([('name', 'Anil'), ('age', 35), ('country', 'India'), ('company', 'Oracle'), ('salary', '400000$'), ('tax', '10'), ('location', 'Bangalore'), ('ranking', 5), ('addr', {'street': '23rd croos', 'district': 'mysore', 'state': 'karnataka'})])
>>> 
>>> 
>>> # ----------------------------------------
>>> 
>>> 
>>> D1 = {'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}
>>> D2 = {'name': 'Sunil', 'age': 36, 'country': 'India', 'company': 'Oracle', 'salary': '350000$'}
>>> D1
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}
>>> D2
{'name': 'Sunil', 'age': 36, 'country': 'India', 'company': 'Oracle', 'salary': '350000$'}
>>> 
>>> DD = {}
>>> DD[D1['name']] = D1
>>> # DD['Anil'] = D1
>>> DD
{'Anil': {'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}}
>>> DD[D2['name']] = D2
>>> DD
{'Anil': {'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}, 'Sunil': {'name': 'Sunil', 'age': 36, 'country': 'India', 'company': 'Oracle', 'salary': '350000$'}}
>>> DD.keys()
dict_keys(['Anil', 'Sunil'])
>>> DD['Anil']
{'name': 'Anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'salary': '300000$'}
>>> DD['Anil']{'country']
SyntaxError: invalid syntax
>>> DD['Anil']['country']
'India'
>>> 
>>> 
>>> # ----------------
>>> 
>>> for person in DD.keys():
	for key in person.keys():
		print( person[key] + ' --------> ' + str(key))

		
Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    for key in person.keys():
AttributeError: 'str' object has no attribute 'keys'
>>> for person in DD.keys():
	for key in DD[person].keys():
		print( person[key] + ' --------> ' + str(key))

		
Traceback (most recent call last):
  File "<pyshell#84>", line 3, in <module>
    print( person[key] + ' --------> ' + str(key))
TypeError: string indices must be integers
>>> for person in DD.keys():
	for key in DD[person].keys():
		print( DD[person][key] + ' --------> ' + str(key))

		
Anil --------> name
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    print( DD[person][key] + ' --------> ' + str(key))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for person in DD.keys():
	for key in DD[person]:
		print(key)

		
name
age
country
company
salary
name
age
country
company
salary
>>> for person in DD.keys():
	for key in DD[person]:
		print(DD[person][key])

		
Anil
35
India
Oracle
300000$
Sunil
36
India
Oracle
350000$
>>> for person in DD.keys():
	print('Record for : ', person, '\n')
	for key in DD[person]:
		print(key + ' ----> ' + str(DD[person][key]))

		
Record for :  Anil 

name ----> Anil
age ----> 35
country ----> India
company ----> Oracle
salary ----> 300000$
Record for :  Sunil 

name ----> Sunil
age ----> 36
country ----> India
company ----> Oracle
salary ----> 350000$
>>> 
