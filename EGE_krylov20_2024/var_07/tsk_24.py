#  минимальная строка
f = open('24.txt')
s = f.read()
N = 10**10

for i in range(1, len(s)):
    if s[i-1] + s[i] == 'AB':
        k = 1
        n = 2
        for j in range(i, len(s) - 1):
            n += 1
            if s[j] + s[j + 1] == 'AB':
                k += 1
            if k == 21:
                N = min(N, n)
                break
print(N)
