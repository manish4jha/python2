'''

try:
    Logic to be tried
except:
    What do you want to do if the exception occurs
else:
    Statements to execute when you tried something and
    no exception occured
finally:
    Statements that define what will happen finally

'''

try:
    f = open(r"C:\Users\Purushotham\Desktop\oracle\d1.dat", "r")
#except Exception as E:
except FileNotFoundError:
    print('The file is not found!')
    #print(E)
else:
    print('File found')
    f.close()
finally:
    print('Done!')
