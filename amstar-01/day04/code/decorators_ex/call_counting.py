def call_counter(func):
    
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

print("Before",succ.calls)
for i in range(10):
    print(succ(i))
    
print("After",succ.calls)


'''

>>> class test(object):
	pass

>>> t = test()
>>> type(t)
<class '__main__.test'>
>>> t.data
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t.data
AttributeError: 'test' object has no attribute 'data'
>>> t.data = 10
>>> t.data
10
>>>

'''
