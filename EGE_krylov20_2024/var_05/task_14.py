def k(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


print(k(4*25**2022 - 2*5**2000 + 125**1011 - 3*5**100 - 660, 5).count('4'))
