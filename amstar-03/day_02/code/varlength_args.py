# Variable Length Arguments

def average(a, b, c):
    return (a + b + c)/3


def average2(L):
    return sum(L)/len(L)

def average3(a, b, *args):
    print(a)
    print(b)
    print(args)
    
def average4(*args):
    return sum(args)/len(args)

def func(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

#print(average(10, 20, 30))
#print(average2([10, 20, 30]))
#print(average2([10, 20, 30, 40, 50]))

print(average4(10, 20, 30))
print(average4(10, 20, 30, 45))
print(average4(10, 20, 30, 67, 89))

# a,b,*c = T


func(10, 20, 30, 45, 78, name='anil', age=35)
