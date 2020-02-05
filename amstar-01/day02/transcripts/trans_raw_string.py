Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.chdir(r"C:\Users\Purushotham\Desktop\Clients\Amstar\amstar-01\day02\examples")
>>> import fibonacci
>>> fibonacci.fib(10)
55
>>> fibonacci.gen_fib(10)
[[0, 1], 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> #######################################
>>> path = "C:\next\text\read\demo.dat"
>>> print(path)
C:
ext	extead\demo.dat
>>> path = "C:\\next\\text\\read\\demo.dat"
>>> print(path)
C:\next\text\read\demo.dat
>>> path = r"C:\next\text\read\demo.dat"
>>> print(path)
C:\next\text\read\demo.dat
>>> ####################################
