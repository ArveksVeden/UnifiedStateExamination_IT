f = open('17.txt')
data = [int(p[:-1]) for p in f]

min_700 = 10**10
for i in data:
    if abs(i) % 1000 == 700:
        if i < min_700:
            min_700 = i

nope = []
for i in range(2, len(data)):
    n1 = int(data[i])
    n2 = int(data[i - 1])
    n3 = int(data[i - 2])
    len_d = [len(str(abs(n1))), len(str(abs(n2))), len(str(abs(n3)))]
    if len_d.count(5) <= 2:
        if n1 + n2 + n3 >= min_700:
            nope.append(n1 + n2 + n3)
print(len(nope), min(nope))
