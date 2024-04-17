f = open('9.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    nope = [i.count(p) for p in i]
    avarage = 0
    max_pov = []
    if nope.count(4) == 4 and nope.count(2) == 2 and nope.count(1) == 2:
        for k in range(len(i)):
            if nope[k] == 1:
                avarage += i[k]
            if nope[k] > 1:
                max_pov.append(i[k])
        avarage /= 2
        if avarage >= max(max_pov):
            cout += 1
print(cout)
