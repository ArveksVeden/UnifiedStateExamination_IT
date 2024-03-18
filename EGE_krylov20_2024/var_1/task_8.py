import itertools
data = [''.join(p) for p in itertools.product('АВИОРТФ', repeat=6)]

n = 1
cout = 0
for i in data:
    if n % 2 == 0 and i[0] != 'О' and i.count('Р') == 2:
        cout += 1
    n += 1
print(cout)