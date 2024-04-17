"""
whole alp: ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


def f(x):
    return int(f'1{x}2{x}3{x}4{x}5', 25) + int(f'2{x}024', 25) + int(f'1{x}099', 25)


nope = []
for x in '0123456789ABCDEFGHIJKLMNO':
    if f(x) % 24 == 0:
        nope.append(x)

print(max(nope), f(max(nope)) / 24)
