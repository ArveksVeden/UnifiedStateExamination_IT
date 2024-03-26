import itertools
print(len([p for p in itertools.product('1234', repeat=3) if ''.join(p).count('2') == 1]))
