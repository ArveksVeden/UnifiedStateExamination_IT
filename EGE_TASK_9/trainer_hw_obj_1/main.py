f = open("nope.txt")
data = [list(map(int, p.split())) for p in f]
res = 0
for i in data:
    nope = [i.count(i[0]), i.count(i[1]), i.count(i[2]), i.count(i[3]), i.count(i[4]), i.count(i[5])]
    if nope.count(3) == 3 and nope.count(1) == 3:
        cout = 0
        summar = 0
        rep_3 = 0
        for j in range(len(nope)):
            if nope[j] == 1:
                cout += 1
                summar += i[j]
            else:
                rep_3 = i[j]
        if (summar / cout) <= rep_3:
            res += 1
print(res)
