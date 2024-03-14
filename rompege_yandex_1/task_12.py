data = []

for n in range(3, 10000):
    s = '5' + '2' * n
    res = 0

    for i in s:
        res += int(i)
    if res == 1685:
        data.append(n)
print(max(data))
