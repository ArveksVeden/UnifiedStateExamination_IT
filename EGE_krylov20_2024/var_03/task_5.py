def k(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(1, 10000):
    r = k(n, 4)
    if n % 4 == 0:
        r += r[-2:]
    else:
        r+= k((n % 4) * 2, 4)
    r = int(r, 4)
    if r >= 1025:
        print(n)
        print(r)
        break
