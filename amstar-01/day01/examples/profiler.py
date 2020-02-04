import datetime

t1 = datetime.datetime.now()

for i in range(1000):
    print('.',end='')

t2 = datetime.datetime.now()

print('It took ', t2 - t1)
