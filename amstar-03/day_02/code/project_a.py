# PROJECT A
# New approach for project A
# It uses function definitions


def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def getprimes(start, end):
    L = []
    for n in range(start, end + 1):
        if(checkprime(n)):
            L.append(n)
    return L

# ---------------------------------

print('PROJECT A', __name__)

if __name__ == '__main__':
    
    a = int(input('Enter a number: '))
    res = checkprime(a)
    if(res):
        print('The number is prime')
    else:
        print('The number is not prime')

    s = 100
    e = 200
    print(getprimes(s, e))

if __name__ == 'project_a':
    print('This module is now being imported!')

    
