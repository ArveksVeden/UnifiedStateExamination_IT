"""

-1
//2

60 -> 10 -> 2

"""


def k(a, b):
    if a == b: return 1
    if a < b: return 0
    return k(a - 1, b) + k(a//2, b)


print(k(60, 2))
