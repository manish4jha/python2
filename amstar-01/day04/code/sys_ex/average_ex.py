import sys

print('The following are the arguments passed from the command line')
print(sys.argv[1:])

args_n = [int(x) for x in sys.argv[1:]]
average = sum(args_n)/ len(args_n)
print("AVERAGE: ", average)
