f = open('17.txt')
data = [int(p[:-1]) for p in f]

nope = []
for i in range(1, len(data)):
    if (data[i-1] + data[i]) >= 50 and data[i-1] > 0 and data[i] > 0:
        nope.append(data[i-1]*data[i])
print(len(nope), min(nope))
