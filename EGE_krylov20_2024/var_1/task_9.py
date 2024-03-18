# ans: 4

f = open('9/9var01.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    nope = [i.count(p) for p in i]
    if nope.count(3) == 6 and nope.count(1) == 2:
        num1 = i[nope.index(1)]
        nope[nope.index(1)] = 0
        num2 = i[nope.index(1)]
        if max(i) == num1 or max(i) == num2:
            cout += 1
print(cout)