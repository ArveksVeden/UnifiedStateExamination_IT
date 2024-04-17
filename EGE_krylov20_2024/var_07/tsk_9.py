f = open('9.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
for i in data:
    flag = False
    if max(i)**2 > (i[0] * i[1] * i[2] * i[3] / max(i)):
        cout += 1
        continue
    nope = sorted(i)
    if nope[3] - nope[2] == nope[2] - nope[1] and nope[2] - nope[1] == nope[1] - nope[0]:
        cout += 1
print(cout)
