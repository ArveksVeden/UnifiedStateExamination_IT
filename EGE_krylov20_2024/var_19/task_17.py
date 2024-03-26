f = open('17.txt')
data = [int(p[:-1]) for p in f]

nope = []
for i in range(1, len(data)):
    if data[i] > 700 or data[i - 1] > 700:
        nope.append(data[i]**2 + data[i - 1]**2)
print(len(nope), max(nope))
