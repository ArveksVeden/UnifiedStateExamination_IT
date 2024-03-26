def is_simp(x):
    return all([x % p != 0 for p in range(2, int(x**0.5) + 1)])


for n in range(2, 10000):
    s = '>' + '1' * 23 + '2' * n + '3' * 25

    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>11', 1)
    summary = 0
    for i in s:
        if i in '0123456789':
            summary += int(i)
    if is_simp(summary):
        print(n)
        break
