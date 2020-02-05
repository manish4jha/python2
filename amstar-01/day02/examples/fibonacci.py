def fib(n):
    """ This function generates the nth
    fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def gen_fib(n):
    """ This function generates a series 
    of n fibonacci numbers"""
    a = 0
    b = 1
    s = []
    if n == 0:
        print('Not a valid argument')
    elif n == 1:
        return s.append(a)
    elif n == 2:
        return s.append([a, b])
    else:
        s.append([a,b])
        for i in range(n-1):
            x = a + b
            s.append(x)
            a = b
            b = x
    return s

###################################################

# Fibonacci Numbers: 0 1 1 2 3 5 8 13 21 ...

if __name__ == '__main__':
    
    print(fib(8))
    print(gen_fib(8))
