from os import walk
f = []
g = walk(r"C:\Users\Purushotham\Desktop\code")
for (dirpath, dirnames, filenames) in g:
 print (dirpath, dirnames, filenames)
 # logic for chaging the file in dirpath
 '''
 L = [ ".sh", ".txt", ".xyz"]
 for ext in L:
    check if the file name ends with the ext
    if you get it:
        do the relavant changes
    '''
 

 
