Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Purushotham\Desktop\code\generator_ex\generator_ex01.py =
>>> vowels()
<generator object vowels at 0x000001DDC3755840>
>>> g = vowels()
>>> next(g)
'a'
>>> next(g)
'e'
>>> next(g)
'i'
>>> next(g)
'o'
>>> next(g)
'u'
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(g)
StopIteration
>>> egen = create_emoticon_generator()
>>> next(egen)
'[//!]'
>>> for i in range(10):
	next(egen)

	
'(:*^)'
'[!?_]'
'(=..)'
'[*@.]'
'<,?+>'
'[/=_]'
'(#?$)'
'(*$+)'
'<_;@>'
'(;#:)'
>>> 
>>> 
>>> 
>>> next(egen)
'(@.+)'
>>> L = [next(egen), next(egen), next(egen)]
>>> 
>>> L
['($~:)', '(!.,)', '[?^@]']
>>> 
= RESTART: C:\Users\Purushotham\Desktop\code\generator_ex\generator_ex01.py =
>>> egen = create_emoticon_generator()
>>> nexy(egen)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nexy(egen)
NameError: name 'nexy' is not defined
>>> next(egen)
'(/$!)'
>>> next(egen)
'[!+*]'
>>> next(egen)
'<?;;>'
>>> next(egen)
'(*^-)'
>>> next(egen)
'(_!@)'
>>> next(egen)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    next(egen)
StopIteration
>>> egen = create_emoticon_generator()
>>> next(egen)
'<^^~>'
>>> 
