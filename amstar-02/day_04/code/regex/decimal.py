import re

expr = '37.0 degree centigrade is equal to +98.6 farhenheit'

pattern = r'-|\+?\d+\.?\d*|\.?\d+'

print (expr)
print ('Trying to find a floating point numbers in the statement...')

match = re.findall(pattern, expr)
if match:
    print ('Following numbers were found', match)
else:
    print ('Seems like there is no floating point number')


# ----------------

'''

'-|\+?  \d+  \.?   \d*  | \.?\d+'

.34
.567

12
+12
-12
12.45
+12.45
-12.45


'''
