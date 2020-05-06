# regex_experiments.py

import re
data = ['ab', 'abc', 'a5e', 'a6f', '123 a6c', 'a5b', 'a55b', 'a555b', 'a5555b',
        'a55555b', 'a555555b', 'amazing', 'a5xbmnop', '1/4', '3+2=5', 'def ghi', 'abc ab']
for item in data:
	m = re.search(r'a(55){2}\D', item)
	if m:
		print (m.group() + ' matched in ' + '\'' + item + '\'')



# 123 a6c


# --------- Senthil Kumar
''''
 m = re.search(r'\w+[ma]\w+[in]', item)
 m = re.search(r'\w+(ma)\w+(in)', item)
 m = re.search(r'\w+ma\w+in', item)

 a5xbmxxcnop
'''

'''
my_var
text_with_space

my_var

myVar
textWithSpace

__name__
__main__

'''

'''
123 a6c
a.c
 a.c
  a.c
   a.c
    a.c
     a.c

'''


