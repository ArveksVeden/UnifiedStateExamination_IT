"""
whole alp: ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


def f(x):
    return (int(f'3{x}2{x}1{x}0{x}1', 19) + int(f'{x}2024', 19) + int(f'1{x}077', 19))


nope = []
for x in '0123456789ABCDEFGHI':
    if f(x) % 18 == 0:
        nope.append(x)
print(f(max(nope)) / 18)
