# Project #2
# Extract all the prime numbers between a user given range

import primemod

if __name__ == "__main__":
    
    start = int(input('Enter the start of the range: '))
    end   = int(input('Enter the end of the range: '))

    '''
    L = []
    for n in range(start, end + 1):
        if(primemod.checkprime(n)):
            L.append(n)
    '''
    
    print('-'*30)
    print("PRIMES")
    print(primemod.getprimes(start, end))


    
