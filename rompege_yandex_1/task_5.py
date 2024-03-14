# ans: 100

def k(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(1, 10000):
    r = k(n, 5)
    if n % 25 == 0:
        r = r[-3:] + r
    else:
        c = k(n % 25, 5)
        r += c
    r = int(r, 5)
    if r > 10000:
        print(n)
        break