import itertools
data = [''.join(p) for p in itertools.product('АГЕИЛНРТ', repeat=5)]

cout = 0
k = 1
for i in data:
    if k % 2 != 0 and i[0] != 'Т' and (i.count('Н') == 1 or i.count('Н') == 2):
        cout += 1
    k += 1
print(cout)
