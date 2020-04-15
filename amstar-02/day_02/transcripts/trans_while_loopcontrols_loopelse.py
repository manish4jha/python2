Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 0
>>> while i < 10:
	print(i, i**2, i**3)
	i = i + 1

	
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
>>> for i in range(0, 10):
	print(i, i**2, i**3)

	
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
>>> i
9
>>> # ----------------------------------------------
>>> 
>>> # LOOP CONTROL STATEMENTS
>>> 
>>> # break -> abruptly makes the loop to exit
>>> # continue -> skips the iteration
>>> # pass -> ignore
>>> 
>>> for i in range(10):
	print(i, end=' ')
	if(i % 6 == 0):
		break

	
0 
>>> for i in range(1, 10):
	print(i, end=' ')
	if(i % 6 == 0):
		break

	
1 2 3 4 5 6 
>>> for i in range(1, 10):
	print(i, end=' ')
	if(i % 6 == 0):
		print('break')
		break
		print('-------')

		
1 2 3 4 5 6 break
>>> for i in range(1, 10):
	if(i % 6 == 0):
		continue
	print(i, end=' ')

	
1 2 3 4 5 7 8 9 
>>> for i in range(1, 10):
	if(i % 6 == 0):
		pass
	print(i, end=' ')

	
1 2 3 4 5 6 7 8 9 
>>> 
>>> 
>>> 
>>> # ------------- Loop else block
>>> 
>>> # Loop can terminate due to two reasons:
>>> # 1. Natural exit
>>> # 2. break
>>> 
>>> for i in range(10):
	print(i, i**2)
else:
	print('Completed!') # The statements in else block will be executed once if the loop exits naturally

	
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
Completed!
>>> for i in range(10):
	print(i, i**2)
	if(i % 3 == 0):
		break
else:
	print('Completed!') # The statements in else block will not be executed  if the loop doesn't exit naturally/ exits because of break statement

	
0 0
>>> for i in range(1, 10):
	print(i, i**2)
	if(i % 3 == 0):
		break
else:
	print('Completed!') # The statements in else block will not be executed  if the loop doesn't exit naturally/ exits because of break statement

	
1 1
2 4
3 9
>>> 
