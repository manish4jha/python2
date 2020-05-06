Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE OPERATIONS
>>> # f = open(<path>,<mode>)
>>> # mode ---> r, w, a, b
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_03\code\students.csv", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students.csv", "r")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> 
>>> # Read commands
>>> # read() --> reads the entire file as a single string
>>> # readline  ---> reads the file line by line
>>> # readlines() ---> reads entire file as a list of line
>>> # tell() ---> Position of the cursor
>>> # seek() ---> Reset the cursor to a give position
>>> 
>>> content = f.read()
>>> content
'name,age,regid,phy,chem,math,bio,avg,rank\nVijay,14,HPE001,99,98,97,96,0,0\nAryan,14,HPE002,98,91,93,96,0,0\nMuni,14,HPE003,97,98,97,94,0,0\nAbhi,14,HPE004,96,93,97,95,0,0\nHemanth,14,HPE005,94,91,93,96,0,0\nGrace,14,HPE006,94,95,96,97,0,0\n'
>>> print(content)
name,age,regid,phy,chem,math,bio,avg,rank
Vijay,14,HPE001,99,98,97,96,0,0
Aryan,14,HPE002,98,91,93,96,0,0
Muni,14,HPE003,97,98,97,94,0,0
Abhi,14,HPE004,96,93,97,95,0,0
Hemanth,14,HPE005,94,91,93,96,0,0
Grace,14,HPE006,94,95,96,97,0,0

>>> type(content)
<class 'str'>
>>> f.readline()
''
>>> f.tell()
241
>>> len(content)
234
>>> f.seek(0)
0
>>> f.tell()
0
>>> f.readline()
'name,age,regid,phy,chem,math,bio,avg,rank\n'
>>> f.readline()
'Vijay,14,HPE001,99,98,97,96,0,0\n'
>>> f.readline()
'Aryan,14,HPE002,98,91,93,96,0,0\n'
>>> f.seek(0)
0
>>> f.seek(f.tell() + 5)
5
>>> f.readline()
'age,regid,phy,chem,math,bio,avg,rank\n'
>>> f.seek(f.tell() + 5)
48
>>> f.readline()
',14,HPE001,99,98,97,96,0,0\n'
>>> f.readline(f.seek(5))
'age,r'
>>> f.seek(5)
5
>>> f.readline(5)
'age,r'
>>> f.readline()
'egid,phy,chem,math,bio,avg,rank\n'
>>> f.readline()
'Vijay,14,HPE001,99,98,97,96,0,0\n'
>>> f.readline(10)
'Aryan,14,H'
>>> f.readline()
'PE002,98,91,93,96,0,0\n'
>>> 
>>> 
>>> f.seek(0)
0
>>> content = f.readlines()
>>> content
['name,age,regid,phy,chem,math,bio,avg,rank\n', 'Vijay,14,HPE001,99,98,97,96,0,0\n', 'Aryan,14,HPE002,98,91,93,96,0,0\n', 'Muni,14,HPE003,97,98,97,94,0,0\n', 'Abhi,14,HPE004,96,93,97,95,0,0\n', 'Hemanth,14,HPE005,94,91,93,96,0,0\n', 'Grace,14,HPE006,94,95,96,97,0,0\n']
>>> for line in content:
	print(line.upper())

	
NAME,AGE,REGID,PHY,CHEM,MATH,BIO,AVG,RANK

VIJAY,14,HPE001,99,98,97,96,0,0

ARYAN,14,HPE002,98,91,93,96,0,0

MUNI,14,HPE003,97,98,97,94,0,0

ABHI,14,HPE004,96,93,97,95,0,0

HEMANTH,14,HPE005,94,91,93,96,0,0

GRACE,14,HPE006,94,95,96,97,0,0

>>> f.seek(0)
0
>>> f.readlines(3)
['name,age,regid,phy,chem,math,bio,avg,rank\n']
>>> f.readlines()
['Vijay,14,HPE001,99,98,97,96,0,0\n', 'Aryan,14,HPE002,98,91,93,96,0,0\n', 'Muni,14,HPE003,97,98,97,94,0,0\n', 'Abhi,14,HPE004,96,93,97,95,0,0\n', 'Hemanth,14,HPE005,94,91,93,96,0,0\n', 'Grace,14,HPE006,94,95,96,97,0,0\n']
>>> 
>>> f.close()
>>> 
>>> 
>>> # -------------------------- Writing into a file
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students2.csv", "w")
>>> 
>>> # write()  -> writes a string
>>> # writelines() -> writes a list of strings
>>> 
>>> f.write('This is a copy of students.csv\n')
31
>>> f.write('-'*90 + '\n')
91
>>> f.close()
>>> 
>>> # ------------------------- Appending into a file
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students2.csv", "a")
>>> 
>>> f.write('\n\n')
2
>>> content = ['Vijay,14,HPE001,99,98,97,96,0,0\n', 'Aryan,14,HPE002,98,91,93,96,0,0\n', 'Muni,14,HPE003,97,98,97,94,0,0\n', 'Abhi,14,HPE004,96,93,97,95,0,0\n', 'Hemanth,14,HPE005,94,91,93,96,0,0\n', 'Grace,14,HPE006,94,95,96,97,0,0\n']
>>> 
>>> f.writelines(content)
>>> f.close()
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\Research\HTML\dev.html", "r")
>>> f.read()
'<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>\n<h4>Heading 4</h4>\n<h5>Heading 5</h5>\n<h6>Heading 6</h6>'
>>> f.seek(0)
0
>>> print(f.read())
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
>>> 
>>> 
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students2.csv", "r")
>>> f.write("New content")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    f.write("New content")
io.UnsupportedOperation: not writable
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students2.csv", "a")
>>> f.write("New content")
11
>>> f.close()
>>> f.close()
>>> 
>>> 
>>> 
>>> # ------------------------------- shutil
>>> 
>>> import shutil
>>> 
>>> src = r"
SyntaxError: EOL while scanning string literal
>>> 
>>> src = r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students2.csv"
>>> dst = r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv"
>>> shutil.copy(src, dst)
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\code\\students3.csv'
>>> 
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle\day_03\code"0
	 
SyntaxError: invalid syntax
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle\day_03\code")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\code'
>>> os.listdir()
['getips_using_regex.py', 'regex_ex.py', 'regex_ex_2.py', 'students.csv', 'students2.csv', 'students3.csv']
>>> "students3.csv" in os.listdir()
True
>>> 
>>> os.path.isfile(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
True
>>> os.path.isfile(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students4.csv")
False
>>> os.path.getctime(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
1588762791.7868521
>>> os.path.getatime(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
1588762791.7888532
>>> os.path.getsize(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
337
>>> os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv")
TypeError: access() missing required argument 'mode' (pos 2)
>>> os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv", "r")
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv", "r")
TypeError: an integer is required (got type str)
>>> os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv", os.R_OK)
True
>>> os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv", os.W_OK)
True
>>> os.access(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\students3.csv", os.X_OK)
True
>>> 
>>> 
>>> # ----------------------------------------------- Anitha
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print("C:\Users\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print("C:\zsers\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt")
C:\zsers\Purushotham\Desktop\oracle\day_03\code
extead	est.txt
>>> f = open("C:\zsers\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt", "r")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    f = open("C:\zsers\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\zsers\\Purushotham\\Desktop\\oracle\\day_03\\code\next\read\test.txt'
>>> print(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt")
C:\Users\Purushotham\Desktop\oracle\day_03\code\next\read\test.txt
>>> 
