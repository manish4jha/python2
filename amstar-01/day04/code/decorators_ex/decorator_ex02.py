def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            #raise Exception("Argument is not an integer")
            print("Arguement should be a positive number")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


'''
for i in range(1,10):
	print(i, factorial(i))

print(factorial(-1))
'''

# Transcript

'''
= RESTART: C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py =
>>> factorial(10)
3628800
>>> factorial(-10)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    factorial(-10)
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 14, in factorial
    return n * factorial(n-1)
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 14, in factorial
    return n * factorial(n-1)
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 14, in factorial
    return n * factorial(n-1)
  [Previous line repeated 990 more times]
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 11, in factorial
    if n == 1:
RecursionError: maximum recursion depth exceeded in comparison
>>> fatorial("a")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fatorial("a")
NameError: name 'fatorial' is not defined
>>> factorial("a")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    factorial("a")
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 14, in factorial
    return n * factorial(n-1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
= RESTART: C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py =
>>> factorial(10)
3628800
>>> factorial(-10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    factorial(-10)
  File "C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py", line 6, in helper
    raise Exception("Argument is not an integer")
Exception: Argument is not an integer
>>> 
= RESTART: C:/Users/Purushotham/Desktop/code/decorators_ex/decorator_ex02.py =
>>> factorial(10)
3628800
>>> factorial(-10)
Arguement should be a positive number
>>> factorial("a")
Arguement should be a positive number
>>> factorial(asdf)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    factorial(asdf)
NameError: name 'asdf' is not defined
>>> 

'''
