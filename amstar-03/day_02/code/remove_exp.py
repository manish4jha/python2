def removefromlist(L, item, pos):
    count = 0
    p = 0
    for i in L:
        if(i == item):
            count += 1
            if(count == pos):
                del L[p]
        p += 1

L = ['red', 'green', 'blue', 'white', 'black', 'white', 'grey', 'white']
print('Before:' )
print(L)
removefromlist(L, 'white', 3)
print('After: ')
print(L)


