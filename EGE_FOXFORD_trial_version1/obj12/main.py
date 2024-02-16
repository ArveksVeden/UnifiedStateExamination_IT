for n in range(10000):
    s = '>' + '0' * 15 +  '1' * n + '2' * 21
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '23>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '3>', 1)
    s = s[:-1]
    res = 0
    for i in s:
        res += int(i)
    if res % 26 == 0:
        print(n)
        break
