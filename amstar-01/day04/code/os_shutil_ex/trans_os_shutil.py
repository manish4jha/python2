Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\code")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\code'
>>> os.mkdir('temp')
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\code'
>>> os.chdir('temp')
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\code\\temp'
>>> os.chdir(os.pardir)
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\code'
>>> import shutil
>>> src = os.path.join(os.getcwd(), 'json_ex01.py')
>>> src
'C:\\Users\\Purushotham\\Desktop\\code\\json_ex01.py'
>>> dest = 'C:\\Users\\Purushotham\\Desktop\\code\\temp\\json_ex01.py'
>>> shutil.copy(src, dest)
'C:\\Users\\Purushotham\\Desktop\\code\\temp\\json_ex01.py'
>>> 
