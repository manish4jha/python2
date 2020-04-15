Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
prime
not prime
prime
not prime
prime
prime
prime
prime
prime
prime
prime
prime
prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 15
The number is not prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 17
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 0
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 1
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 2
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 15
The number is not prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 17
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 0
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 1
The number is prime
>>> 
===== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/prime.py =====
Enter a number: 2
The number is prime
>>> 
= RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_histogram.py =

On a dark desert highway
Cool wind in my hair
Warm smell of colitas
Rising up through the air
Up ahead in the distance
I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway
I heard the mission bell
And I was thinkin' to myself
'This could be heaven or this could be hell
Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here
Her mind is Tiffany-twisted
She got the Mercedes Benz, uh
She got a lot of pretty, pretty boys
That she calls friends
How they…

>>> set(text)
{'i', 'p', '-', 'l', 'M', 'w', 'z', 'n', 'T', 'S', 'y', 'b', 'u', 'r', 'v', 'k', 'e', 'a', 'g', ' ', 's', 'c', 'O', 'd', 'U', 'A', "'", 'R', 'C', ')', '(', 'H', 'I', ',', '…', 'o', 'h', '\n', 'W', 't', 'Y', 'P', 'f', 'B', 'm'}
>>> type(text)
<class 'str'>
>>> list(text)
['\n', 'O', 'n', ' ', 'a', ' ', 'd', 'a', 'r', 'k', ' ', 'd', 'e', 's', 'e', 'r', 't', ' ', 'h', 'i', 'g', 'h', 'w', 'a', 'y', '\n', 'C', 'o', 'o', 'l', ' ', 'w', 'i', 'n', 'd', ' ', 'i', 'n', ' ', 'm', 'y', ' ', 'h', 'a', 'i', 'r', '\n', 'W', 'a', 'r', 'm', ' ', 's', 'm', 'e', 'l', 'l', ' ', 'o', 'f', ' ', 'c', 'o', 'l', 'i', 't', 'a', 's', '\n', 'R', 'i', 's', 'i', 'n', 'g', ' ', 'u', 'p', ' ', 't', 'h', 'r', 'o', 'u', 'g', 'h', ' ', 't', 'h', 'e', ' ', 'a', 'i', 'r', '\n', 'U', 'p', ' ', 'a', 'h', 'e', 'a', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'd', 'i', 's', 't', 'a', 'n', 'c', 'e', '\n', 'I', ' ', 's', 'a', 'w', ' ', 'a', ' ', 's', 'h', 'i', 'm', 'm', 'e', 'r', 'i', 'n', 'g', ' ', 'l', 'i', 'g', 'h', 't', '\n', 'M', 'y', ' ', 'h', 'e', 'a', 'd', ' ', 'g', 'r', 'e', 'w', ' ', 'h', 'e', 'a', 'v', 'y', ' ', 'a', 'n', 'd', ' ', 'm', 'y', ' ', 's', 'i', 'g', 'h', 't', ' ', 'g', 'r', 'e', 'w', ' ', 'd', 'i', 'm', '\n', 'I', ' ', 'h', 'a', 'd', ' ', 't', 'o', ' ', 's', 't', 'o', 'p', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'e', ' ', 'n', 'i', 'g', 'h', 't', '\n', 'T', 'h', 'e', 'r', 'e', ' ', 's', 'h', 'e', ' ', 's', 't', 'o', 'o', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'd', 'o', 'o', 'r', 'w', 'a', 'y', '\n', 'I', ' ', 'h', 'e', 'a', 'r', 'd', ' ', 't', 'h', 'e', ' ', 'm', 'i', 's', 's', 'i', 'o', 'n', ' ', 'b', 'e', 'l', 'l', '\n', 'A', 'n', 'd', ' ', 'I', ' ', 'w', 'a', 's', ' ', 't', 'h', 'i', 'n', 'k', 'i', 'n', "'", ' ', 't', 'o', ' ', 'm', 'y', 's', 'e', 'l', 'f', '\n', "'", 'T', 'h', 'i', 's', ' ', 'c', 'o', 'u', 'l', 'd', ' ', 'b', 'e', ' ', 'h', 'e', 'a', 'v', 'e', 'n', ' ', 'o', 'r', ' ', 't', 'h', 'i', 's', ' ', 'c', 'o', 'u', 'l', 'd', ' ', 'b', 'e', ' ', 'h', 'e', 'l', 'l', '\n', 'T', 'h', 'e', 'n', ' ', 's', 'h', 'e', ' ', 'l', 'i', 't', ' ', 'u', 'p', ' ', 'a', ' ', 'c', 'a', 'n', 'd', 'l', 'e', '\n', 'A', 'n', 'd', ' ', 's', 'h', 'e', ' ', 's', 'h', 'o', 'w', 'e', 'd', ' ', 'm', 'e', ' ', 't', 'h', 'e', ' ', 'w', 'a', 'y', '\n', 'T', 'h', 'e', 'r', 'e', ' ', 'w', 'e', 'r', 'e', ' ', 'v', 'o', 'i', 'c', 'e', 's', ' ', 'd', 'o', 'w', 'n', ' ', 't', 'h', 'e', ' ', 'c', 'o', 'r', 'r', 'i', 'd', 'o', 'r', '\n', 'I', ' ', 't', 'h', 'o', 'u', 'g', 'h', 't', ' ', 'I', ' ', 'h', 'e', 'a', 'r', 'd', ' ', 't', 'h', 'e', 'm', ' ', 's', 'a', 'y', '\n', 'W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'H', 'o', 't', 'e', 'l', ' ', 'C', 'a', 'l', 'i', 'f', 'o', 'r', 'n', 'i', 'a', '\n', 'S', 'u', 'c', 'h', ' ', 'a', ' ', 'l', 'o', 'v', 'e', 'l', 'y', ' ', 'p', 'l', 'a', 'c', 'e', ' ', '(', 's', 'u', 'c', 'h', ' ', 'a', ' ', 'l', 'o', 'v', 'e', 'l', 'y', ' ', 'p', 'l', 'a', 'c', 'e', ')', '\n', 'S', 'u', 'c', 'h', ' ', 'a', ' ', 'l', 'o', 'v', 'e', 'l', 'y', ' ', 'f', 'a', 'c', 'e', '\n', 'P', 'l', 'e', 'n', 't', 'y', ' ', 'o', 'f', ' ', 'r', 'o', 'o', 'm', ' ', 'a', 't', ' ', 't', 'h', 'e', ' ', 'H', 'o', 't', 'e', 'l', ' ', 'C', 'a', 'l', 'i', 'f', 'o', 'r', 'n', 'i', 'a', '\n', 'A', 'n', 'y', ' ', 't', 'i', 'm', 'e', ' ', 'o', 'f', ' ', 'y', 'e', 'a', 'r', ' ', '(', 'a', 'n', 'y', ' ', 't', 'i', 'm', 'e', ' ', 'o', 'f', ' ', 'y', 'e', 'a', 'r', ')', '\n', 'Y', 'o', 'u', ' ', 'c', 'a', 'n', ' ', 'f', 'i', 'n', 'd', ' ', 'i', 't', ' ', 'h', 'e', 'r', 'e', '\n', 'H', 'e', 'r', ' ', 'm', 'i', 'n', 'd', ' ', 'i', 's', ' ', 'T', 'i', 'f', 'f', 'a', 'n', 'y', '-', 't', 'w', 'i', 's', 't', 'e', 'd', '\n', 'S', 'h', 'e', ' ', 'g', 'o', 't', ' ', 't', 'h', 'e', ' ', 'M', 'e', 'r', 'c', 'e', 'd', 'e', 's', ' ', 'B', 'e', 'n', 'z', ',', ' ', 'u', 'h', '\n', 'S', 'h', 'e', ' ', 'g', 'o', 't', ' ', 'a', ' ', 'l', 'o', 't', ' ', 'o', 'f', ' ', 'p', 'r', 'e', 't', 't', 'y', ',', ' ', 'p', 'r', 'e', 't', 't', 'y', ' ', 'b', 'o', 'y', 's', '\n', 'T', 'h', 'a', 't', ' ', 's', 'h', 'e', ' ', 'c', 'a', 'l', 'l', 's', ' ', 'f', 'r', 'i', 'e', 'n', 'd', 's', '\n', 'H', 'o', 'w', ' ', 't', 'h', 'e', 'y', '…', '\n']
>>> text.count('dark')
1
>>> text.count('she')
4
>>> text.split()
['On', 'a', 'dark', 'desert', 'highway', 'Cool', 'wind', 'in', 'my', 'hair', 'Warm', 'smell', 'of', 'colitas', 'Rising', 'up', 'through', 'the', 'air', 'Up', 'ahead', 'in', 'the', 'distance', 'I', 'saw', 'a', 'shimmering', 'light', 'My', 'head', 'grew', 'heavy', 'and', 'my', 'sight', 'grew', 'dim', 'I', 'had', 'to', 'stop', 'for', 'the', 'night', 'There', 'she', 'stood', 'in', 'the', 'doorway', 'I', 'heard', 'the', 'mission', 'bell', 'And', 'I', 'was', "thinkin'", 'to', 'myself', "'This", 'could', 'be', 'heaven', 'or', 'this', 'could', 'be', 'hell', 'Then', 'she', 'lit', 'up', 'a', 'candle', 'And', 'she', 'showed', 'me', 'the', 'way', 'There', 'were', 'voices', 'down', 'the', 'corridor', 'I', 'thought', 'I', 'heard', 'them', 'say', 'Welcome', 'to', 'the', 'Hotel', 'California', 'Such', 'a', 'lovely', 'place', '(such', 'a', 'lovely', 'place)', 'Such', 'a', 'lovely', 'face', 'Plenty', 'of', 'room', 'at', 'the', 'Hotel', 'California', 'Any', 'time', 'of', 'year', '(any', 'time', 'of', 'year)', 'You', 'can', 'find', 'it', 'here', 'Her', 'mind', 'is', 'Tiffany-twisted', 'She', 'got', 'the', 'Mercedes', 'Benz,', 'uh', 'She', 'got', 'a', 'lot', 'of', 'pretty,', 'pretty', 'boys', 'That', 'she', 'calls', 'friends', 'How', 'they…']
>>> 
= RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_histogram.py =

On a dark desert highway
Cool wind in my hair
Warm smell of colitas
Rising up through the air
Up ahead in the distance
I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway
I heard the mission bell
And I was thinkin' to myself
'This could be heaven or this could be hell
Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here
Her mind is Tiffany-twisted
She got the Mercedes Benz, uh
She got a lot of pretty, pretty boys
That she calls friends
How they…

{'On': 1, 'a': 7, 'dark': 1, 'desert': 1, 'highway': 1, 'Cool': 1, 'wind': 1, 'in': 3, 'my': 2, 'hair': 1, 'Warm': 1, 'smell': 1, 'of': 5, 'colitas': 1, 'Rising': 1, 'up': 2, 'through': 1, 'the': 10, 'air': 1, 'Up': 1, 'ahead': 1, 'distance': 1, 'I': 6, 'saw': 1, 'shimmering': 1, 'light': 1, 'My': 1, 'head': 1, 'grew': 2, 'heavy': 1, 'and': 1, 'sight': 1, 'dim': 1, 'had': 1, 'to': 3, 'stop': 1, 'for': 1, 'night': 1, 'There': 2, 'she': 4, 'stood': 1, 'doorway': 1, 'heard': 2, 'mission': 1, 'bell': 1, 'And': 2, 'was': 1, "thinkin'": 1, 'myself': 1, "'This": 1, 'could': 2, 'be': 2, 'heaven': 1, 'or': 1, 'this': 1, 'hell': 1, 'Then': 1, 'lit': 1, 'candle': 1, 'showed': 1, 'me': 1, 'way': 1, 'were': 1, 'voices': 1, 'down': 1, 'corridor': 1, 'thought': 1, 'them': 1, 'say': 1, 'Welcome': 1, 'Hotel': 2, 'California': 2, 'Such': 2, 'lovely': 3, 'place': 1, '(such': 1, 'place)': 1, 'face': 1, 'Plenty': 1, 'room': 1, 'at': 1, 'Any': 1, 'time': 2, 'year': 1, '(any': 1, 'year)': 1, 'You': 1, 'can': 1, 'find': 1, 'it': 1, 'here': 1, 'Her': 1, 'mind': 1, 'is': 1, 'Tiffany-twisted': 1, 'She': 2, 'got': 2, 'Mercedes': 1, 'Benz,': 1, 'uh': 1, 'lot': 1, 'pretty,': 1, 'pretty': 1, 'boys': 1, 'That': 1, 'calls': 1, 'friends': 1, 'How': 1, 'they…': 1}
>>> d = {}
>>> d['name'] = 'raj'
>>> d
{'name': 'raj'}
>>> d['raj'] = 1
>>> d
{'name': 'raj', 'raj': 1}
>>> if 'raj' in d.keys():
	d['raj'] = d['raj'] + 1

	
>>> d
{'name': 'raj', 'raj': 2}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)dfgsdf
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py", line 11, in <module>
    D.setdefault(dl[0], float(dl[1]))
IndexError: list index out of range
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py", line 21, in <module>
    avgs.sort(reverse=True)         # Descending sort of all the averages
AttributeError: 'dict_values' object has no attribute 'sort'
>>> d = {'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
>>> d.keys()
dict_keys(['Raj', 'Sunil', 'Mahesh'])
>>> i = d.keys()
>>> i.sort()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    i.sort()
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> i = list(d.keys())
>>> i.sort()
>>> i
['Mahesh', 'Raj', 'Sunil']
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
{'Raj': {'avg': 345.0, 'rank': 3}, 'Sunil': {'avg': 500.0, 'rank': 1}, 'Mahesh': {'avg': 455.0, 'rank': 2}}
>>> D['Sunil']['rank']
1
>>> D['Mahesh']['rank']
2
>>> D['Raj']['rank']
3
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
{'Raj': {'avg': 345.0, 'rank': 3}, 'Sunil': {'avg': 500.0, 'rank': 1}, 'Mahesh': {'avg': 455.0, 'rank': 2}}
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py", line 35, in <module>
    print('NAME : ' + key + ' RANK: ' + D[key]['rank'])
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0}
{'Raj': {'avg': 345.0, 'rank': 3}, 'Sunil': {'avg': 500.0, 'rank': 1}, 'Mahesh': {'avg': 455.0, 'rank': 2}}
NAME : Raj RANK: 3
NAME : Sunil RANK: 1
NAME : Mahesh RANK: 2
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)Anil, 500
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0, 'Anil': 500.0}
{'Raj': {'avg': 345.0, 'rank': 4}, 'Sunil': {'avg': 500.0, 'rank': 1}, 'Mahesh': {'avg': 455.0, 'rank': 3}, 'Anil': {'avg': 500.0, 'rank': 1}}
NAME : Raj RANK: 4
NAME : Sunil RANK: 1
NAME : Mahesh RANK: 3
NAME : Anil RANK: 1
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/averages_and_ranks.py 
Enter student name and average marks(name,average)(q to quit)Raj, 345
Enter student name and average marks(name,average)(q to quit)Sunil, 500
Enter student name and average marks(name,average)(q to quit)Mahesh, 455
Enter student name and average marks(name,average)(q to quit)Anil, 500
Enter student name and average marks(name,average)(q to quit)q
{'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0, 'Anil': 500.0}
{'Raj': {'avg': 345.0, 'rank': 3}, 'Sunil': {'avg': 500.0, 'rank': 1}, 'Mahesh': {'avg': 455.0, 'rank': 2}, 'Anil': {'avg': 500.0, 'rank': 1}}
NAME : Raj RANK: 3
NAME : Sunil RANK: 1
NAME : Mahesh RANK: 2
NAME : Anil RANK: 1
>>> d
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d = {'Raj': 345.0, 'Sunil': 500.0, 'Mahesh': 455.0, 'Anil': 500.0}
>>> d.keys()
dict_keys(['Raj', 'Sunil', 'Mahesh', 'Anil'])
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values([345.0, 500.0, 455.0, 500.0])
>>> d.items()
dict_items([('Raj', 345.0), ('Sunil', 500.0), ('Mahesh', 455.0), ('Anil', 500.0)])
>>> #####
>>> 
>>> s = 'python'
>>> 
>>> # o n y h t p
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
['python', 'laptop', 'computer', 'cherries', 'oxygen', 'carbon', 'apples']
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
['laptop', 'apples', 'python', 'oxygen', 'computer', 'cherries', 'carbon']
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
['cherries', 'laptop', 'python', 'apples', 'oxygen', 'carbon', 'computer']
>>> s = 'cherries'
>>> l = list(s)
>>> l
['c', 'h', 'e', 'r', 'r', 'i', 'e', 's']
>>> import random
>>> random.shuffle(l)
>>> l
['s', 'c', 'r', 'r', 'e', 'e', 'i', 'h']
>>> ''.join(l)
'scrreeih'
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
----------------------------------------
		THE WORD JUMBLE GAME
----------------------------------------
GUESS THIS WORD:  onarbc
>>> carbon
Correct guess!
GUESS THIS WORD:  ecirrseh
>>> cherries
Correct guess!
GUESS THIS WORD:  ygexno
>>> oxygen
Correct guess!
GUESS THIS WORD:  lepspa
>>> apples
Correct guess!
GUESS THIS WORD:  tpynho
>>> python
Correct guess!
GUESS THIS WORD:  mcuorpte
>>> correct
Incorrect guess..
GUESS THIS WORD:  plaopt
>>> pilot
Incorrect guess..
------------------------------
SCORE :  5
Your playing is excellent
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
----------------------------------------
		THE WORD JUMBLE GAME
----------------------------------------
GUESS THIS WORD:  cshrreei
>>> cherrier
Incorrect guess..
GUESS THIS WORD:  alsppe
>>> mangoe
Incorrect guess..
GUESS THIS WORD:  ppaolt
>>> pilot
Incorrect guess..
GUESS THIS WORD:  acbron
>>> carbon
Correct guess!
GUESS THIS WORD:  phonyt
>>> python
Correct guess!
GUESS THIS WORD:  euoprcmt
>>> cat
Incorrect guess..
GUESS THIS WORD:  goxeyn
>>> generic
Incorrect guess..
------------------------------
SCORE :  2
Give a better try next time
>>> 
== RESTART: C:/Users/Purushotham/Desktop/oracle/day_02/code/word_jumble.py ==
----------------------------------------
	THE WORD JUMBLE GAME
----------------------------------------
GUESS THIS WORD:  oppatl
>>> laptop
Correct guess!
GUESS THIS WORD:  tuocermp
>>> computer
Correct guess!
GUESS THIS WORD:  onygxe
>>> oxygen
Correct guess!
GUESS THIS WORD:  bnaroc
>>> carbon
Correct guess!
GUESS THIS WORD:  apples
>>> apples
Correct guess!
GUESS THIS WORD:  rsiehrec
>>> cherry
Incorrect guess..
GUESS THIS WORD:  hpoynt
>>> hypnotic
Incorrect guess..
------------------------------
SCORE :  5
Your playing is excellent
>>> s = 'mississippi'
>>> s.find('ss')
2
>>> # (2,4)
>>> s[2:4]
'ss'
>>> s[5:7]
'ss'
>>> # 'ss' ---> (2, 4)
>>> # 'ss' ---> (5, 7)
