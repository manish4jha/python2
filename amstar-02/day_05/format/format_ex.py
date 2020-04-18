Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 10
>>> print('SUM: ', s)
SUM:  10
>>> print('SUM: %d', s)
SUM: %d 10
>>> print('SUM: %d' % s)
SUM: 10
>>> print('SUM: %d %d' % (s, s**2))
SUM: 10 100
>>> print('Values: %d %f %s' % (10, 1.3, 'hello'))
Values: 10 1.300000 hello
>>> print('Values: {} {} {}'.format(10, 1.3, 'hello'))
Values: 10 1.3 hello
>>> print('SUM: ', s, 'Next value: ', 143)
SUM:  10 Next value:  143
>>> print('Values: {0} {1} {2}'.format(10, 1.3, 'hello'))
Values: 10 1.3 hello
>>> print('Values: {2} {1} {1}'.format(10, 1.3, 'hello'))
Values: hello 1.3 1.3
>>> print('Values: {2} {1} {1}'.format(a=10, b=1.3, c='hello'))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('Values: {2} {1} {1}'.format(a=10, b=1.3, c='hello'))
IndexError: tuple index out of range
>>> print('Values: {a} {c} {b}'.format(a=10, b=1.3, c='hello'))
Values: 10 hello 1.3
>>> print('Values: {a:5} {c:10} {b:6}'.format(a=10, b=1.3, c='hello'))
Values:    10 hello         1.3
>>> print('Values: {a:<5} {c:^10} {b:>6}'.format(a=10, b=1.3, c='hello'))
Values: 10      hello       1.3
>>> template = 'Values: \n{a:<5} \n{c:^10} \n{b:>6}'
>>> template
'Values: \n{a:<5} \n{c:^10} \n{b:>6}'
>>> template.format(a='python', b='perl', c='java')
'Values: \npython \n   java    \n  perl'
>>> print(template.format(a='python', b='perl', c='java'))
Values: 
python 
   java    
  perl
>>> print(template.format(a='python', b='perl', c='ruby'))
Values: 
python 
   ruby    
  perl
>>> L = ['python', 'scala', 'clojure']
>>> print(template.format(a=L[0], b=L[1], c=L[2]))
Values: 
python 
 clojure   
 scala
>>> template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:2}'
>>> print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
>>> for i in range(10):
	print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))

	
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
>>> def report():
	print('-'*80)
	print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
	print('-'*80)
	for i in range(10):
		print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
	print('-'*80)

	
>>> report()
--------------------------------------------------------------------------------
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
--------------------------------------------------------------------------------
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
REGID    | NAME       | AGE | P   | C   | M   | B   | AVG    | R 
--------------------------------------------------------------------------------
>>> 
