Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 45
>>> print(x)
45
>>> print('Value is : ', x)
Value is :  45
>>> print ('value is %d' % x)
value is 45
>>> print('The values is {}'.format(x))
The values is 45
>>> DD = {'anil' : {'avg':500, 'rank':1},'sunil' : {'avg':505, 'rank':2} }
>>> for person in DD.keys():
	print(person)

	
anil
sunil
>>> DD.keys()
dict_keys(['anil', 'sunil'])
>>> DD['anil']['avg']
500
>>> for person in DD.keys():
	print(DD[person])

	
{'avg': 500, 'rank': 1}
{'avg': 505, 'rank': 2}
>>> for person in DD.keys():
	print(DD[person]['avg'])

	
500
505
>>> 
