f = open('9.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    nope = [i.count(p) for p in i]
    if nope.count(3) == 3 and nope.count(2) == 2 and nope.count(1) == 3:
        avarage = 0
        pov = 0
        for k in range(len(i)):
            if nope[k] == 1:
                avarage += i[k]
            if nope[k] == 3:
                pov = i[k]
        avarage /= 3
        if avarage <= pov:
            cout += 1
print(cout)
