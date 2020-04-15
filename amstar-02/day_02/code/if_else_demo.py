# Program to find the differece between
# two user given numbers

# Input

a = input('Enter a number: ')
b = input('Enter another number: ')

# Process

res = int(a) - int(b)

# Output

print('----------------------')
print('DIFFERENCE: ', abs(res))


if res > 0:
    print('The difference is positive')
    if res > 5:
        print('The difference is also greater than 5')
elif res < 0:
    print('The difference is negative')
else:
    print('The difference is zero')
    #print('Thank you!')



print('Thank you!')
