"""
alp all: ABCDEFGHIJKLMNOPQRSTUVWXYZ

0123456789ABCDEFGHIJKLMNO
"""


def f(x, y):
    return int(f'13{y}{x}5', 26) + int(f'24{y}13', 26)


nope = []
for x in '0123456789ABCDEFGHIJKLMNOP':
    if all(f(x, y) % 8 == 0 for y in '0123456789ABCDEFGHIJKLMNOP'):
        nope.append(x)
print(nope)
print(max(nope))

print(f(max(nope), 2) / 8)
