Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2020, 4, 17, 13, 22, 6, 446570)
>>> t.year
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.year
NameError: name 't' is not defined
>>> t = datetime.now()
>>> t.year
2020
>>> t.month
4
>>> t.day
17
>>> t.hour
13
>>> t.minute
22
>>> t.second
32
>>> t1 = datetime.now()
>>> t1 - t
datetime.timedelta(seconds=37, microseconds=70681)
>>> t
datetime.datetime(2020, 4, 17, 13, 22, 32, 293843)
>>> type(t)
<class 'datetime.datetime'>
>>> t.strftime("%a")
'Fri'
>>> t.strftime("%B")
'April'
>>> t.strftime("%A")
'Friday'
>>> f = "%A, %d/%B/%Y, %H:%M:%S"
>>> t.strftime(f)
'Friday, 17/April/2020, 13:22:32'
>>> filename = t.strftime(f)+'.log'
>>> filename
'Friday, 17/April/2020, 13:22:32.log'
>>> 
