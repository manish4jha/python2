# PROJECT A
# Detecting if a number is prime or not


'''
for <var> in <iter>:
    <statements>
else:
    <statements>

while <condition>:
    <statements>
else:
    <statements>

Loop exits because of two scenarios:
1. elements in the <iter> is exhausted, or
   <condition> becomes false (NATURAL EXIT)
2. Loop can also exit because of the break statement

If the loop exits naturally, statements under else
block will execute once

If the loop exits because of a break statement,
then statements under else block will not be executed

'''

# Program to find out if a number is prime

# input

n = int(input('Enter a number: '))

'''
# process

prime = True
for i in range(2, n):
    if(n % i == 0):
        prime = False
        break
     
# output

if(prime):  # prime == True
    print('The number is prime')
else:
    print('The number is not prime')
'''

for i in range(2, n):
    if(n % i == 0):
        print('The number is not prime')
        break
else:
    print('The number is prime')
