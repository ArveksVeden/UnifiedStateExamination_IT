f = open('17.txt')
data = [int(p[:-1]) for p in f]

max_num = max(data)
nope = []
for i in range(1, len(data)):
    if data[i] + data[i - 1] == max_num:
        nope.append(data[i]**2 + data[i-1]**2)
print(len(nope), max(nope))
