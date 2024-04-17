f = open('17_03.txt')
data = [int(p[:-1]) for p in f]

max_90 = 0
for i in data:
    if abs(i) % 100 == 90:
        if i > max_90:
            max_90 = i

nope = []
for i in range(2, len(data)):
    n1 = data[i]
    n2 = data[i - 1]
    n3 = data[i - 2]

    if len(str(abs(n1))) == 4 or len(str(abs(n2))) == 4 or len(str(abs(n3))) == 4:
        if n1 + n2 + n3 > max_90:
            nope.append(n1 + n2 + n3)
print(len(nope), min(nope))
