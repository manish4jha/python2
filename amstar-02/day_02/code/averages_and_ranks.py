# get the student and their average marks from the user
# based on the average marks print the rank for every student

# input

D = {}
while True:
    data = input('Enter student name and average marks(name,average)(q to quit)')
    if data == 'q':
        break
    else:
        dl = data.split(',')
        D.setdefault(dl[0], float(dl[1]))


print(D)

# process

avgs = list(set(list(D.values())))         # Get all the "unique" averages
avgs.sort(reverse=True)         # Descending sort of all the averages

rank = 1
for avg in avgs:  # [500.0, 455.0, 345.0]
    for key in D.keys():    #{'Raj':345.0,'Sunil':500.0,'Mahesh':455.0,'Anil':500.0}
        if (D[key] == avg):
            D[key] = {'avg':D[key], 'rank': rank}
    rank += 1

print(D)

# Output

for key in D.keys():
    print('NAME : ' + key + ' RANK: ' + str(D[key]['rank']))

    
