Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:\Users\Purushotham\Desktop\code\oop\special_methods.py =====
>>> acc
<__main__.Account object at 0x00000282CE393208>
>>> str(acc)
'<__main__.Account object at 0x00000282CE393208>'
>>> print(acc)
<__main__.Account object at 0x00000282CE393208>
>>> repr(acc)
'<__main__.Account object at 0x00000282CE393208>'
>>> t = [1,2,3]
>>> str(t)
'[1, 2, 3]'
>>> repr(t)
'[1, 2, 3]'
>>> pritn(t)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pritn(t)
NameError: name 'pritn' is not defined
>>> print(t)
[1, 2, 3]
>>> 
===== RESTART: C:\Users\Purushotham\Desktop\code\oop\special_methods.py =====
>>> acc
Account('Billy Jean', 1000000)
>>> str(acc)
'Account of Billy Jean with starting amount: 1000000'
>>> repr(acc)
"Account('Billy Jean', 1000000)"
>>> print(acc)
Account of Billy Jean with starting amount: 1000000
>>> len(acc)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    len(acc)
TypeError: object of type 'Account' has no len()
>>> acc[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    acc[0]
TypeError: 'Account' object is not subscriptable
>>> acc[1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    acc[1]
TypeError: 'Account' object is not subscriptable
>>> 
===== RESTART: C:\Users\Purushotham\Desktop\code\oop\special_methods.py =====
>>> len(acc)
5
>>> acc[0]
20
>>> acc[1]
-10
>>> acc[2]
50
>>> for i in acc:
	print(i)

	
20
-10
50
-20
30
>>> reversed(acc)
[30, -20, 50, -10, 20]
>>> acc.balance
1000070
>>> 
===== RESTART: C:\Users\Purushotham\Desktop\code\oop\special_methods.py =====
>>> acc1000070
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    acc1000070
NameError: name 'acc1000070' is not defined
>>> acc
Account('Billy Jean', 1000000)
>>> acc2 = Account('John Wick', 3000000)
>>> acc == acc2
False
>>> acc < acc2
True
>>> acc2 > acc
True
>>> acc != acc2
True
>>> 
