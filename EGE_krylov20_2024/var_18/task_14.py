"""
whole alp: ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
nope = []
for x in '0123456789ABCDEFG':
    res = int(f'135{x}9', 17) + int(f'9{x}531', 17)
    if res % 9 == 0:
        nope.append(x)
print(max(nope))
