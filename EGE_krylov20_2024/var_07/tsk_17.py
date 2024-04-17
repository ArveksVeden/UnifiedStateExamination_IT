f = open('17.txt')
data = [int(p[:-1]) for p in f]

max_el = max(data)
nope = []
for i in range(2, len(data)):
    n1 = data[i]
    n2 = data[i-1]
    n3 = data[i-2]
    if (n1 % 10 == 0 and n2 % 10 != 0 and n3 % 10 != 0) or \
       (n1 % 10 != 0 and n2 % 10 == 0 and n3 % 10 != 0) or \
       (n1 % 10 != 0 and n2 % 10 != 0 and n3 % 10 == 0):
        if n1 + n2 + n3 < max_el:
            nope.append(n1 + n2 + n3)
print(len(nope), max(nope))
