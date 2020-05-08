Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> s = "python"
>>> f = 1.45
>>> print('Value: ', f)
Value:  1.45
>>> print("The measurement was", f, " units")
The measurement was 1.45  units
>>> print("The measurement was %f units" % (f))
The measurement was 1.450000 units
>>> print("The measurement was %f units" % (a))
The measurement was 10.000000 units
>>> print("The measurement was %.sf units" % (a))
The measurement was f units
>>>  print("The measurement was %.2f units" % (a))
 
SyntaxError: unexpected indent
>>> print("The measurement was %.2f units" % (a))
The measurement was 10.00 units
>>> print("The measurement was %.2f units, with %d degrees of freedom" % (f, a))
The measurement was 1.45 units, with 10 degrees of freedom
>>> print("The measurement was %.2f units, with %d degrees of freedom" % (12.345, 3))
The measurement was 12.35 units, with 3 degrees of freedom
>>> 
>>> 
>>> 'My name is {} and age is {}'.format('Raj', 35)
'My name is Raj and age is 35'
>>> 'My name is {0} and age is {1}'.format('Raj', 35)
'My name is Raj and age is 35'
>>> 'My name is {1} and age is {0}'.format('Raj', 35)
'My name is 35 and age is Raj'
>>> 'My name is {name} and age is {age}'.format(name='Raj', age=35)
'My name is Raj and age is 35'
>>> 'My name is {name:10} and age is {age:5}'.format(name='Raj', age=35)
'My name is Raj        and age is    35'
>>> 'My name is {name:>10} and age is {age:<5}'.format(name='Raj', age=35)
'My name is        Raj and age is 35   '
>>> 'My name is {name:^10} and age is {age:^5}'.format(name='Raj', age=35)
'My name is    Raj     and age is  35  '
>>> 
>>> 
>>> template = 'My name is {name:^10} and age is {age:^5}'
>>> template.format(name='Raj', age=35)
'My name is    Raj     and age is  35  '
>>> template.format(name='Anil', age=25)
'My name is    Anil    and age is  25  '
>>> 
