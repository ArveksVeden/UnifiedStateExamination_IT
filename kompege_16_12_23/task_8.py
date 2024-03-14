#  6561 - 59048 - i (перевести i в 9-ю)


def k(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]

#  012345678
cout = 0

for i in range(6561, 59049):
    s = k(i, 9)
    if s.count('5') == 1 and '00' not in s and '11' not in s and '22' not in s and \
       '33' not in s and '44' not in s and '55' not in s and '66' not in s and \
       '77' not in s and '88' not in s:
        cout += 1
print(cout)
