import itertools
data = [''.join(p) for p in itertools.product('АЕИКЛПР', repeat=6)]

i = 1
cout = 0
for s in data:
    if i % 2 == 0 and s[0] != 'К' and s.count('И') >= 2:
        cout += 1
    i += 1
print(cout)
