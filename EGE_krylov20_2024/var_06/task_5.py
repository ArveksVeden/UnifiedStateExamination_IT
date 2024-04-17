nope = []
for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '0'
    else:
        r += '1'
    if r.count('1') % 3 == 0:
        r = '11' + r[2:]
    else:
        r = '10' + r[2:]
    r = int(r, 2)
    if r <= 37:
        nope.append(n)
print(max(nope))
