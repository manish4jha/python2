# Experiment to invoke ipconfig -all
# Capture the output
# Extract the physical addresses

import subprocess
content = subprocess.check_output('ipconfig -all', shell=True)

type(content) # This will be in the form of bytes
content = content.decode() # Converts that into a string

'''
s = 'python'
b = bytes(s, 'utf-8')
type(b)

s2 = b.decode() # Converts that into a string
'''

# Method 1

text = content.split('\r\n')
type(text) # It should be a list
for line in text:
    if(line.strip().startswith('Physical')):
        print(line)


# Method 2

import re
pattern = r'(\w\w-){5}(\w\w)' # Pattern for physical address

# Line by line search approach
for line in text:
    m = re.search(pattern, line)
    if m:
        print(line)  # print(m.group())

# Extract all at once using findall
phy = re.findall(pattern, content)
print(phy)
