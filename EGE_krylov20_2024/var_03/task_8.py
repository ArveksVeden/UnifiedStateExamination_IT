import itertools
data = [''.join(p) for p in itertools.product('АГИЛМНОФ', repeat=5)]

k = 1
cout = 0
for i in data:
    if k % 2 != 0 and i[0] != 'Н' and i.count('О') <= 1:
        cout += 1
    k += 1
print(cout)
