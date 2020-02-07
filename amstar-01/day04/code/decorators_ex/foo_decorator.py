def our_decorator(func):  # func is the function object
    def function_wrapper(x): # x is the arguments that func object has
        print("Before calling " + func.__name__)
        func(x.upper()[::-1])
        print("After calling " + func.__name__)
    return function_wrapper



@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("hi")

'''
print("We call foo before decoration:")
foo("Hi")
    
print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)
'''
