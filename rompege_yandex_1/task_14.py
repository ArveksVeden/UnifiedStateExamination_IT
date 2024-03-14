def k(n, b):
    if n < 0:
        n = abs(n)
    s = ''
    while n > 0:
        if n % b < 10:
            s += str(n % b)
        else:
            s += '*'
        n //= b
    return s[::-1]

res = k(18 * 7**108 - 5 * 49**76 + 343**35 - 50, 49)

cout = 0
for i in res:
    if i in '0123456789':
        cout += int(i)
print(cout)