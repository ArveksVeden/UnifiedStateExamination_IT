# 3382
f = open('9.txt')
data = [list(map(int, p.split())) for p in f]


cout = 0
for i in data:
    c = [p for p in i]
    nope = [c.count(c[0]), c.count(c[1]), c.count(c[2]), c.count(c[3]), \
            c.count(c[4]), c.count(c[5]), c.count(c[6])]
    if nope.count(2) == 6:
        nepov = c[nope.index(1)]
        del c[nope.index(1)]
        sr_ar = (min(c) + max(c)) / 2
        if sr_ar < nepov:
            cout += 1
print(cout)