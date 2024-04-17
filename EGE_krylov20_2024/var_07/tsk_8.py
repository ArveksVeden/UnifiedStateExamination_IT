import itertools
data = [''.join(p) for p in itertools.product('КНОРСЯ', repeat=6)]
k = 1
for i in data:
    if i.count('К') <= 3 and i.count('Я') == 2:
        print(k, i)
        break
    k += 1
