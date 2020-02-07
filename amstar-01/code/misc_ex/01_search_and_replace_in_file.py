import fileinput
import os

file = 'sample.txt'

with fileinput.FileInput(file, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('xyz', 'abc'), end='')

file.close ()
