# ans: 24
data = []
for n in range(1, 100000):
    r = bin(n)[2:]

    if n % 2 == 0:
        r += r[-2:]
    else:
        r = r[::-1] + '1'
        r = r[::-1] + '0'
    r = int(r, 2)
    if r < 100:
        data.append(n)
print(max(data))