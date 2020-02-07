'''
The glob module finds all the pathnames matching a specified pattern according to the
rules used by the Unix shell, although results are returned in arbitrary order.
'''

import glob
dirList = glob.glob(r"C:\Users\Purushotham\Desktop\code\tkinter_ex\*.py")
for d in dirList:
 print (d)
