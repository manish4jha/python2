Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "My name is {} and age is {}".format("Chris", 45)
'My name is Chris and age is 45'
>>> "My name is {0} and age is {1}".format("Chris", 45)
'My name is Chris and age is 45'
>>> "My name is {0:20} and age is {1:5}".format("Chris", 45)
'My name is Chris                and age is    45'
>>> "My name is {0:>20} and age is {1:<5}".format("Chris", 45)
'My name is                Chris and age is 45   '
>>> "My name is {0:^20} and age is {1:^5}".format("Chris", 45)
'My name is        Chris         and age is  45  '
>>> "My name is {name:^20} and age is {age:^5}".format(name="Chris", age=45)
'My name is        Chris         and age is  45  '
>>> template = "My name is {name:^20} and age is {age:^5}"
>>> template.format(name="Chris", age=45)
'My name is        Chris         and age is  45  '
>>> template.format(name="John", age=35)
'My name is         John         and age is  35  '
>>> 
