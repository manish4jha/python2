Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/checkprime_application.py 
Enter a number:12
The number is not prime
Enter the start point: 100
Enter the end point: 200
PRIMES: 
[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/checkprime_application.py 
Enter the start point: 100
Enter the end point: 500
PRIMES: 
[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
>>> 3/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    3/0
ZeroDivisionError: division by zero
>>> '34' + 435
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    '34' + 435
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 23
0.5217391304347826
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 0
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py", line 4, in <module>
    res = n1/n2
ZeroDivisionError: division by zero
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 34
0.35294117647058826
All done!!
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 0
0 not allowed as the divisor
All done!!
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 0
0 not allowed as the divisor
All done!!
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/amstar-01/day02/examples/exceptions_handling.py 
Enter a number: 12
Enter another number: 0
division by zero
0 not allowed as the divisor
All done!!
>>> def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

>>> KelvinToFahrenheit(273)
32.0
>>> KelvinToFahrenheit(0)
-459.40000000000003
>>> KelvinToFahrenheit(-30)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    KelvinToFahrenheit(-30)
  File "<pyshell#3>", line 2, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
>>> 
