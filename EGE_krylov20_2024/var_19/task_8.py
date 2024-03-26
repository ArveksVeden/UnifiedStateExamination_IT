import itertools
print(len([p for p in itertools.product('123456', repeat=5) if ''.join(p).count('1') == 1]))
