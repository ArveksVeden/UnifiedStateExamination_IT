import itertools
data = [''.join(p) for p in itertools.product('0123456789', repeat=4) if p[0] != '0']


cout = 0
for s in data:
    nope = [s.count(p) for p in s]
    if nope.count(2) == 2 and ('11' in s or '00' in s or '22' in s or '33' in s or '44' in s or '55' in s or \
                               '66' in s or '77' in s or '88' in s or '99' in s):
        cout += 1
print(cout)
