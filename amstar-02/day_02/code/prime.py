# Program to determine if the user input number
# is prime or not

# input

n = int(input('Enter a number: '))

'''
# process

prime = True
for x in range(2,n):
    if n % x == 0:
        prime = False
        break

# output

if(prime): # if(prime == True)
    print('The number is prime')
else:
    print('The number is not prime')
    
'''

# Pythonic way!!!

for x in range(2,n):
    if n % x == 0:
        print('The number is not prime')
        break
else:
    print('The number is prime')


    
