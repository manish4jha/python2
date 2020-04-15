Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> TC = [100, 45, 60, 98]
>>> TF = []
>>> for t in TC:
	TF.append(t * 1.8 + 32)

	
>>> TF
[212.0, 113.0, 140.0, 208.4]
>>> # ---- map()
>>> TC
[100, 45, 60, 98]
>>> tf = map(lambda t : t * 1.8 + 32, TC)
>>> tf
<map object at 0x00000273C1561320>
>>> list(tf)
[212.0, 113.0, 140.0, 208.4]
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> # ------ filter()
>>> 
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> F = []
>>> for n in L:
	if( n % 2 == 1 ):
		F.append(n)

		
>>> F
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> f = filter(lambda n : (n % 2 == 1), L)
>>> f
<filter object at 0x00000273C15A6BA8>
>>> list(f)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> f = filter(lambda n : (n % 2 == 0), L)
>>> list(f)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> f
<filter object at 0x00000273C15D86D8>
>>> for n in f:
	print(n, end=' ')

	
>>> f
<filter object at 0x00000273C15D86D8>
>>> f = filter(lambda n : (n % 2 == 0), L)
>>> for n in f:
	print(n*2, end=-' ')

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    print(n*2, end=-' ')
TypeError: bad operand type for unary -: 'str'
>>> f = filter(lambda n : (n % 2 == 0), L)
>>> for n in f:
	print(n*2, end=' ')

	
0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 104 108 112 116 120 124 128 132 136 140 144 148 152 156 160 164 168 172 176 180 184 188 192 196 
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> t = map(lambda n : (n % 2 == 0), L)
>>> list(t)
[True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> 
>>> 
>>> # -------- zip()
>>> 
>>> t1 = ('anil', 'sunil', 'raj')
>>> t2 = ('mysore', 'bangalore', 'noida')
>>> t = zip(t1, t2)
>>> t
<zip object at 0x00000273C15E3408>
>>> list(t)
[('anil', 'mysore'), ('sunil', 'bangalore'), ('raj', 'noida')]
>>> dict(t)
{}
>>> t = zip(t1, t2)
>>> dict(t)
{'anil': 'mysore', 'sunil': 'bangalore', 'raj': 'noida'}
>>> tuple(t)
()
>>> list(t)
[]
>>> t = zip(t1, t2)
>>> t
<zip object at 0x00000273C15E31C8>
>>> zip(*t)
<zip object at 0x00000273C15DF6C8>
>>> tz = zip(*t)
>>> tz
<zip object at 0x00000273C15E3408>
>>> list(tz)
[]
>>> t = zip(t1, t2)
>>> tz = zip(*t)
>>> list(tz)
[('anil', 'sunil', 'raj'), ('mysore', 'bangalore', 'noida')]
>>> 
>>> 
>>> # -------
>>> 
>>> t = map(lambda n : (n % 2 == 0), L)
>>> list(t)
[True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> list(t)
[]
>>> # ------ in all the above discussed functions, it must be noted that once the return map/filter/zip object is untilized by any other function or process, it it destroyed. That would mean you will not be able to use it once again. It you need those values, either store in a variable or recall the respective function
>>> 
