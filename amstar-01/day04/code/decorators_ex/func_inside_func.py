'''
def c2f(n):
    return "Avengers"
'''

def func():

    def c2f(n):
        return "Avengers"
    
    return c2f



# Transcript

'''
>>> f = func()
>>> type(func)
<class 'function'>
>>> f(10)
50.0
>>> f(100)
212.0
>>> 
 RESTART: C:/Users/Purushotham/Desktop/code/decorators_ex/func_inside_func.py 
>>> f = func()
>>> f
<function func.<locals>.c2f at 0x000001F184C9D6A8>
>>> f(9)
'Avengers'
>>> f(10)
'Avengers'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/code/decorators_ex/func_inside_func.py 
>>> f = func()
>>> f (10)
'Avengers'
>>>


'''
