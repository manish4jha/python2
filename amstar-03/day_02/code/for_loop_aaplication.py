colors = ['computer', 'laptop', 'mobile', 'desktop']

# D = {'red':{'length':3, 'r':1, 'e':1, 'd':1 }}

D = {}
for color in colors:
    D2 = {'length':len(color)}
    for ch in set(color):
        D2.setdefault(ch, color.count(ch))
    
    D.setdefault(color, D2)

print(D)
