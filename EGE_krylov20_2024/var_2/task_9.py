f = open('9/9var2.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    nope = [i.count(p) for p in i]
    if nope.count(2) == 6 and nope.count(1) == 2:
        if min(nope) != i[nope.index(2)]:
            cout += 1
print(cout)
