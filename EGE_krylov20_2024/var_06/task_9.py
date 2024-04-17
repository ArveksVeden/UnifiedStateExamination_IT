f = open('9.txt')
data = [list(map(int, p.split())) for p in f]

cout = 0
nope = []
for i in data:
    n1 = i[0]
    n2 = i[1]
    n3 = i[2]
    n4 = i[3]
    if (sum(i) - min(i)) / min(i) > 5:
        if n1 * n2 == n3 * n4 or\
           n1 * n3 == n2 * n4 or\
           n2 * n3 == n1 * n4 or\
           n4 * n1 == n2 * n3:
            cout += 1
print(cout)
