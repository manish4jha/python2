Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # map(), filter() and zip()
>>> # comprehensions
>>> # lambda functions
>>> 
>>> TC = [100, 34, 45, 67, 78]
>>> TF = []
>>> for temp in TC:
	TF.append(temp * 1.8 + 32)

	
>>> TF
[212.0, 93.2, 113.0, 152.60000000000002, 172.4]'
>>> def conv2f(temp):
	return temp * 1.8 + 32

>>> TF2 = map(conv2f, TC)
>>> TF2
<map object at 0x0000029498066CC0>
>>> list(TF2)
[212.0, 93.2, 113.0, 152.60000000000002, 172.4]
>>> for temp in TC:
	TF.append(temp * 1.8 + 32)

	
>>> 
>>> 
>>> L = list(range(1, 1000))
>>> def div5(x):
	return (x % 5 == 0)

>>> F = filter(div5, L)
>>> F
<filter object at 0x00000294980A16D8>
>>> list(F)
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 795, 800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850, 855, 860, 865, 870, 875, 880, 885, 890, 895, 900, 905, 910, 915, 920, 925, 930, 935, 940, 945, 950, 955, 960, 965, 970, 975, 980, 985, 990, 995]
>>> from project_a import checkprime
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    from project_a import checkprime
ModuleNotFoundError: No module named 'project_a'
>>> import sys
>>> sys.path
['', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\Pythonwin']
>>> 
=== RESTART: C:\Users\Purushotham\Desktop\oracle\day_02\code\project_a.py ===
PROJECT A __main__
Enter a number: 34
The number is not prime
[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> sys.path
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sys.path
NameError: name 'sys' is not defined
>>> import sys
>>> sys.path
['C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\code', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\Pythonwin']
>>> from project_a import checkprime
PROJECT A project_a
This module is now being imported!
>>> F = filter(checkprime, L)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    F = filter(checkprime, L)
NameError: name 'L' is not defined
>>> L = list(range(1, 1000))
>>> F = filter(checkprime, L)
>>> F
<filter object at 0x0000025F40738438>
>>> list(F)
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
>>> 
>>> 
>>> T1 = ('anil', 'sunil', 'raj')
>>> T2 = ('bangalore', 'mysore', 'kolar')
>>> T3 = zip(T1, T2)
>>> T3
<zip object at 0x0000025F4049F688>
>>> list(T3)
[('anil', 'bangalore'), ('sunil', 'mysore'), ('raj', 'kolar')]
>>> zip(*L3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    zip(*L3)
NameError: name 'L3' is not defined
>>> zip(*T3)
<zip object at 0x0000025F40766108>
>>> list(zip(*T3))
[]
>>> T3 = zip(T1, T2)
>>> list(zip(*T3))
[('anil', 'sunil', 'raj'), ('bangalore', 'mysore', 'kolar')]
>>> T1 = ('anil', 'sunil', 'raj', 'mohan')
>>> zip(T1, T2)
<zip object at 0x0000025F4049CCC8>
>>> list(zip(T1, T2))
[('anil', 'bangalore'), ('sunil', 'mysore'), ('raj', 'kolar')]
>>> T1
('anil', 'sunil', 'raj', 'mohan')
>>> T2
('bangalore', 'mysore', 'kolar')
>>> dict((zip(T1, T2)))
{'anil': 'bangalore', 'sunil': 'mysore', 'raj': 'kolar'}
>>> 
>>> 
>>> 
>>> def div5(x):
	return (x % 5)

>>> L = list(range(100))
>>> F = filter(div5, L)
>>> F
<filter object at 0x0000025F40770B00>
>>> list(F)
[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99]
>>> def div5(x):
	return (x % 5 == 0)

>>> F = filter(div5, L)
>>> list(F)
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> 
>>> L = ['red', 'green', 'blue', 'marron']
>>> def findr(s):
	return ('r' in s)

>>> F = filter(findr, L)
>>> list(F)
['red', 'green', 'marron']
>>> 
>>> 
>>> 
>>> # ------- lambda functions
>>> 
>>> lambda x,y : x + y
<function <lambda> at 0x0000025F40792A60>
>>> f = lambda x,y : x + y
>>> type(F)
<class 'filter'>
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f('hello', ' oracle')
'hello oracle'
>>> f([1,2,3],['a', 'b', 'c'])
[1, 2, 3, 'a', 'b', 'c']
>>> 
>>> 
>>> TC = [100, 34, 45, 67, 78]
>>> TF = map(lambda t : t * 1.8 + 32, TC)
>>> list(TF)
[212.0, 93.2, 113.0, 152.60000000000002, 172.4]
>>> L = ['red', 'green', 'blue', 'marron']
>>> F = filter(lambda s : 'r' in s, L)
>>> list(F)
['red', 'green', 'marron']
>>> 
>>> 
>>> L = ['apples', 'goat', 'zebra', 'cat', 'banana']
>>> L.sort()
>>> L
['apples', 'banana', 'cat', 'goat', 'zebra']
>>> L.sort(key=lambda e : e[-1])
>>> L
['banana', 'zebra', 'apples', 'cat', 'goat']
>>> 
>>> 
>>> 
>>> # ------------------- comprehensions
>>> 
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> LT = []
>>> for n in L:
	temp = (n, n**2m, n**3)
	
SyntaxError: invalid syntax
>>> for n in L:
	temp = (n, n**2, n**3)
	LT.append(temp)

	
>>> LT
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> 
>>> C = [(x, x**2, x**3) for x in L]
>>> C
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> # Comprehension syntax: [<expr> <loop> <condition>]
>>> 
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> O = [x for x in L if x % 2 == 1]
>>> O
[1, 3, 5, 7, 9]
>>> O = [x**2 for x in L if x % 2 == 1]
>>> O
[1, 9, 25, 49, 81]
>>> L = list(range(11, 100))
>>> L
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> T = (x for x in L if int(str(x)[1]) + int(str(x)[0]) == 8)
>>> T
<generator object <genexpr> at 0x0000025F407417C8>
>>> list(T)
[17, 26, 35, 44, 53, 62, 71, 80]
>>> 
>>> L = ['red', 'green', 'blue', 'white']
>>> D = { key:len(key) for key in L }
>>> D
{'red': 3, 'green': 5, 'blue': 4, 'white': 5}
>>> n = 345
>>> len(str(n))
3
>>> L = list(range(1, 100))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>>  L = list(range(1, 105))
 
SyntaxError: unexpected indent
>>> L = list(range(1, 105))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]
>>> T = [x  for x in L  if ((len(str(x)) == 2) and (int(str(x)[1]) + int(str(x)[0]) == 8))]
>>> T
[17, 26, 35, 44, 53, 62, 71, 80]
>>> 
>>> 
>>> L = [1,2,3,4,5]
>>> T = [i**2 for i in L if i == 3]
>>> T
[9]
>>> T = [ i**2 if i == 3 else i for i in L]
>>> T
[1, 2, 9, 4, 5]
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> T = [x**2 for x in L if x % 2 == 0]
>>> T
[4, 16, 36, 64, 100]
>>> T = [x**2 if x == 6 else x for x in L if x % 2 == 0]
>>> T
[2, 4, 36, 8, 10]
>>> 
>>> 
>>> 
>>> # --------------------------- word histogram
>>> 
>>> text = "This method is useful for form submissions where a user want to bookmark the result"
>>> words = text.split()
>>> words
['This', 'method', 'is', 'useful', 'for', 'form', 'submissions', 'where', 'a', 'user', 'want', 'to', 'bookmark', 'the', 'result']
>>> D = []
>>> for word in words:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
Traceback (most recent call last):
  File "<pyshell#177>", line 2, in <module>
    if(word in D.keys()):
AttributeError: 'list' object has no attribute 'keys'
>>> D = {}
>>> for word in words:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

>>> D
{'This': 1, 'method': 1, 'is': 1, 'useful': 1, 'for': 1, 'form': 1, 'submissions': 1, 'where': 1, 'a': 1, 'user': 1, 'want': 1, 'to': 1, 'bookmark': 1, 'the': 1, 'result': 1}
>>> 
>>> from collections import Counter
>>> z = Counter(words)
>>> z
Counter({'This': 1, 'method': 1, 'is': 1, 'useful': 1, 'for': 1, 'form': 1, 'submissions': 1, 'where': 1, 'a': 1, 'user': 1, 'want': 1, 'to': 1, 'bookmark': 1, 'the': 1, 'result': 1})
>>> L = ['red', 'red', 'green', 'blue', 'red', 'blue']
>>> z = Counter(words)
>>> z
Counter({'This': 1, 'method': 1, 'is': 1, 'useful': 1, 'for': 1, 'form': 1, 'submissions': 1, 'where': 1, 'a': 1, 'user': 1, 'want': 1, 'to': 1, 'bookmark': 1, 'the': 1, 'result': 1})
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'blue': 2, 'green': 1})
>>> 
