# Some program to demonstrate multiple statements in if.. else.. block

# input

a = int(input('Enter a number: '))

# process/output

if (a > 10 and a % 5 == 0):
	print('a is greater than 10')
	print('a is also a multiple of 5')
else:
	if(a > 10):
		print('a is greater than 10')
	elif(a % 5 == 0):
		print('a is divisible by 5')
	else:
		print('No sure of the result')

	print('Inside else')

print('Thank you! Out of if block')

# This is a single line comment

'''

C:\Users\Purushotham\Desktop\oracle\day_01\code>python if_else_multiple_statements.py
Enter a number: 15
a is greater than 10
a is also a multiple of 5
Thank you! Out of if block

C:\Users\Purushotham\Desktop\oracle\day_01\code>python if_else_multiple_statements.py
Enter a number: 12
a is greater than 10
Inside else
Thank you! Out of if block

'''