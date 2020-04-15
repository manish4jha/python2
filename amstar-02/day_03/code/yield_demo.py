def abc():
    yield 'a'
    yield 'b'
    yield 'c'


def nextSquare():
    print('INitializing')
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True:
        print('Before Yield')
        yield i*i
        print('After Yield')
        i += 1  # Next execution resumes  
                # from this point

# --------------------------------

'''
x = abc()
print(x)
'''

'''
for y in abc():
    print(y)
'''
G = nextSquare()
print('First')
for n in G:
    if( n > 100):
        break
    print(n)

G = nextSquare()
print('Second')
for n in G:
    if( n > 100):
        break
    print(n)   
    
    
