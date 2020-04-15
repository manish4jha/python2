import subprocess

content = subprocess.check_output('ipconfig -all', shell=True)
content = content.decode()
print(type(content))
content = content.split('\r\n')

for line in content:
    if('Physical' in line):
        print(line)

#---------------- alternative

content = filter(lambda line : 'Physical' in line, content)
print(content)
