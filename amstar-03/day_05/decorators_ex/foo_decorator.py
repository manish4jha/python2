

def our_decorator(func):  # func is the function object

    def function_wrapper(x, y): # x is the arguments that func object has
        #print("Before calling " + func.__name__)
        func(str(x).upper()[::-1], '')
        func(str(y).upper()[::-1], '')
        #print("After calling " + func.__name__)

    return function_wrapper

# --------------------------------------------------------

'''
def foo(x, y):
    print("Hi, foo has been called with " + str(x))

if __name__ == "__main__":
    print("We call foo before decoration:")
    foo("avengers", "GoG")

    print("We now decorate foo with f:")
    foo = our_decorator(foo)

    print("We call foo after decoration:")
    foo("avengers", "GoG")
'''

# ----------------------------------------


@our_decorator
def foo(x, y):
    print("Hi, foo has been called with " + str(x))

foo("Avengers", "GoG")
