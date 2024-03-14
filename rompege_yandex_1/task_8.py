import itertools
data = [''.join(p) for p in itertools.product('АЕКПТЧ', repeat = 7)]

cout = 0
flag = False
for i in data:
    if i == 'АПТЕЧКА':
        flag = True
        continue
    if flag and i != 'ПЕЧАТКА':
        cout += 1
    if i == 'ПЕЧАТКА':
        break
print(cout)
