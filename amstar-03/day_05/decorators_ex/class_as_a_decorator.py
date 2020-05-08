# Using class as a decorator

class decorator2(object):
    
    def __init__(self, f):
        self.f = f
        print('Decorator creation: ', self.f)
        
    def __call__(self, x):
        print("Decorating", self.f.__name__)
        self.f(x.upper())

@decorator2
def foo(x):
    print("inside foo()", x)

foo('Hello')
