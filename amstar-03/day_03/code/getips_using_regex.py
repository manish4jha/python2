# Invoke the system command from python shell
# Apply regular expressions to extract all the IP addresses

import subprocess
import re

# ----------------------------------------------------

def getCmdOutput(cmd, mode):
    content = subprocess.check_output(cmd, shell=True)
    content = content.decode()
    if (mode == 0): # return a string
        return content
    else:
        lines = content.split('\r\n')
        return lines

def getSpans(output, pattern):
    mobjs = re.finditer(pattern, output)
    spans = []
    if mobjs:
        for obj in mobjs:
            spans.append(obj.span())
    return spans
    

# ----------------------------------------------------

# 192.168.1.1

ipPattern = r"(\d{1,3}\.){3}\d{1,3}"

# 06 May 2020 09:10:22

datePattern = r"\d{1,2}\s\w+\s\d{4}\s(\d{2}:){2}\d{2}"

# ----------------------------------------------------

'''
output = getCmdOutput("ipconfig -all", 0)
mobjs = re.finditer(ipPattern, output)
for obj in mobjs:
	print(obj.group(), obj.span())
'''


output = getCmdOutput("ipconfig -all", 0)
spans  = getSpans(output, datePattern)
print(spans)

# cross check

print('CROSS CHECKING: ')
print(getCmdOutput("ipconfig -all", 0)[1979: 1999])

