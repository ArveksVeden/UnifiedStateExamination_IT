f = open('nope.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for _ in data:
    nope = [_.count(_[0]), _.count(_[1]), _.count(_[2]), _.count(_[3]), _.count(_[4]), _.count(_[5])]
    if nope.count(3) == 3 and nope.count(1) == 3:
        sr_nepov = 0
        num_3 = 0
        for i in range(len(nope)):
            if nope[i] == 3:
                num_3 = _[i]
            else:
                sr_nepov += _[i]
        if (sr_nepov / 3) <= num_3:
            cout += 1
print(cout)
