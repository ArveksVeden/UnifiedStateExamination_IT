def k(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


cout = 0
for i in range(256, 1023 + 1):
    s = k(i, 4)
    if s.count('3') == 1 and '03' not in s and '30' not in s:
        cout += 1
print(cout)
