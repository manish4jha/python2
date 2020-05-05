# PROJECT B
# Take several numbers from the user
# Separate the prime numbers, odd numbers and even numbers
# from the user input

import project_a

#from project_a import checkprime
#from project_a import *

print('PROJECT B', __name__)

# inputs

L = []

uin = ''
print('Enter numerical data:')
print('-'*40)
while uin != 'q':
    uin = input('-> ')
   
    if(uin.isdigit()):
        L.append(int(uin))
    
    #L.append(uin)

print('-'*40)
print('INPUT NUMBERS: ')
print(L)

# process

primes = []
for n in L:
    if(project_a.checkprime(n)):
        primes.append(n)

odds = []
evens = []
for n in L:
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)


# output
print('-'*40)
print('PRIMES: ')
print(primes)

print('Odd Numbers: ')
print(odds)

print('Even Numbers: ')
print(evens)

    
