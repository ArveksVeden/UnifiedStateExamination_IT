"""
whole alp: ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


def f(x, y):
    return int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)


nope = []
for x in '0123456789ABCDEFGHIJK':
    if all(f(x, y) % 18 == 0 \
           for y in '0123456789ABCDEFGHIJK'):
                nope.append(x)
print(min(nope), f(min(nope), 5) / 18)
