# Program to print the multiplication table

n = int(input('Enter a number: '))

'''
for i in range(1, 11):
    print(str(n) + ' X ' + str(i) + ' = ' + str(n*i))

'''

i = 1
while i <= 10:
    print(str(n) + ' X ' + str(i) + ' = ' + str(n*i))
    i += 1

    
