f = open('k9.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    nope = [i.count(i[0]), i.count(i[1]), i.count(i[2]), i.count(i[3]), i.count(i[4]), i.count(i[5])]
    if nope.count(3) == 3 and nope.count(1) == 3:
        sum_nepov = 0
        sr_pov = 0
        for j in range(len(nope)):
            if nope[j] == 3:
                sr_pov = i[j]
            else:
                sum_nepov += i[j]
        if sum_nepov <= sr_pov:
            cout += 1
print(cout)
