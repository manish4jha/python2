import os
os.chdir(r'C:\Users\Purushotham\Desktop\Clients\Amstar\amstar-01\day02\examples')

from checkprime import checkprime

start = int(input('Enter the start point: '))
end = int(input('Enter the end point: '))

primes = []
for n in range(start, end + 1):
    if(checkprime(n)):
        primes.append(n)

print('PRIMES: ')
print(primes)
