# Project #1
# Check if a number is prime or not

def checkprime(n):
    for x in range(2, n):
        if(n % x == 0):
            return False
    return True


def getprimes(start, end):
    primeList = []
    for n in range(start, end + 1):
        if(checkprime(n)):
            primeList.append(n)
    return primeList

#################################

if __name__ == "__main__":
    
    a = int(input('Enter a number: '))

    if(checkprime(a) == True):
        print('This is a prime number')
    else:
        print('This is not a prime number')
    
