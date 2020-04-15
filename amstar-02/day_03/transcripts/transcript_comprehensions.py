Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N = []
>>> for i in range(100):
	if(i % 3 == ):
		
SyntaxError: invalid syntax
>>> N = []
>>> for i in range(100):
	if(i % 3 == 0):
		
SyntaxError: multiple statements found while compiling a single statement
>>> N = []
>>> for i in range(100):
	if(i % 3 == 0):
		N.append(i)

		
>>> N
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> # ------- Comprehensions
>>> 
>>> # LC = [<expr> <loop> <condition>]
>>> 
>>> LC = [x for x in range(100) if (x % 3 == 0)]
>>> LC
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> LC = [x**2 for x in range(100) if (x % 3 == 0)]
>>> LC
[0, 9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025, 2304, 2601, 2916, 3249, 3600, 3969, 4356, 4761, 5184, 5625, 6084, 6561, 7056, 7569, 8100, 8649, 9216, 9801]
>>> 
>>> 
>>> L = ['123', '456', '678']
>>> LN = map(lambda x : int(x), L)
>>> LN
<map object at 0x0000022E7FB01EB8>
>>> list(LN)
[123, 456, 678]
>>> f = lambda x : int(x)
>>> f('123')
123
>>> int('123')
123
>>> LN = map(f, L)
>>> list(LN)
[123, 456, 678]
>>> LN = map(int, L)
>>> list(LN)
[123, 456, 678]
>>> 
>>> N = [12, 34, 56, 78, 89]
>>> NS = [ int(str(x)[0]) + int(str(x)[1]) for x in N]
>>> NS
[3, 7, 11, 15, 17]
>>> 
>>> N = [2, 3, 5, 7, 8]
>>> NC = [ (y, y**2, y**3) for x in N]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    NC = [ (y, y**2, y**3) for x in N]
  File "<pyshell#36>", line 1, in <listcomp>
    NC = [ (y, y**2, y**3) for x in N]
NameError: name 'y' is not defined
>>> NC = [ (y, y**2, y**3) for y in N]
>>> NC
[(2, 4, 8), (3, 9, 27), (5, 25, 125), (7, 49, 343), (8, 64, 512)]
>>> 
>>> S = ['apples', 'grapes', 'coconut', 'pumpkin']
>>> from collection import Counter
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    from collection import Counter
ModuleNotFoundError: No module named 'collection'
>>> from collections import Counter
>>> DC = {s : dict(Counter(s)) for s in S}
>>> DC
{'apples': {'a': 1, 'p': 2, 'l': 1, 'e': 1, 's': 1}, 'grapes': {'g': 1, 'r': 1, 'a': 1, 'p': 1, 'e': 1, 's': 1}, 'coconut': {'c': 2, 'o': 2, 'n': 1, 'u': 1, 't': 1}, 'pumpkin': {'p': 2, 'u': 1, 'm': 1, 'k': 1, 'i': 1, 'n': 1}}
>>> 
>>> NC = [ (x, y) for x in range(10) for y in range(10) if ( x + y == 10)]
>>> NC
[(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
>>> 
>>> L = [1, 2, 3, 4, 5]
>>> LC = [x**2 for x in L if x == 3]
>>> LC
[9]
>>> LC = [x**2 if x == 3 else x for x in L]
>>> LC
[1, 2, 9, 4, 5]
>>> 
