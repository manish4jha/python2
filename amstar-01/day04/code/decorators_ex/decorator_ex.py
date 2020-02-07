def our_decorator(func):
    def function_wrapper(a):
        print("Before calling " + func.__name__)
        print(a)
        func(a)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + x + y + z)


foo("Hi")
