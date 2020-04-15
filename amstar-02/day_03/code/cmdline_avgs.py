import sys

# print(sys.argv)

def averages(L):
    nL = list(map(lambda x : int(x), L))
    return sum(nL)/len(nL)

def avgs(L):
    s = 0
    for n in L:
        s += int(n)
    return s/len(L)

print('Average : ', avgs(sys.argv[1:]))


# --------------- outputs on the command line

'''
C:\Users\Purushotham\Desktop\oracle\day_03\code>python cmdline_avgs.py 10 20 30 40
Average :  25.0

C:\Users\Purushotham\Desktop\oracle\day_03\code>python cmdline_avgs.py 10 20 30 40 43 54 657 87 98
Average :  115.44444444444444

C:\Users\Purushotham\Desktop\oracle\day_03\code>python cmdline_avgs.py 10 20 30 40 43 54 657 87 98
Average :  115.44444444444444

C:\Users\Purushotham\Desktop\oracle\day_03\code>python sysargs.py apples banana cherries
['sysargs.py', 'apples', 'banana', 'cherries']

'''
