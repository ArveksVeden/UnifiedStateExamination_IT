nope = []
for n in range(100000):
    r = ''
    for i in bin(n)[2:]:
        r += i * 2
    r = int(r, 2)
    if r > 32:
        nope.append(r)
print(min(nope))
