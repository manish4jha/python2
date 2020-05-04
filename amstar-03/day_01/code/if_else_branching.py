# Program to print the absolute difference of two numbers

# input

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

# process

res = a - b

# output

print('-'*30)
print('DIFFERENCE: ', abs(a - b))

if(res > 0):
    print('The result is positive')
elif(res < 0):
    print('The result is negative')
else:
    print('The result is zero')
