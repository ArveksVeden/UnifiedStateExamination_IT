f = open('17.txt')
data = [int(p[:-1]) for p in f]

max_chet = 0
for i in data:
    if i % 2 == 0 and i > max_chet:
        max_chet = i

print(max_chet)

nope = []
for i in range(1, len(data)):
    if data[i] + data[i - 1] == max_chet:
        nope.append(data[i]**2 + data[i-1]**2)
print(len(nope), max(nope))
