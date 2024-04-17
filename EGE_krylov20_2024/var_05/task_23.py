"""
-1
//2
50 -> 20 -> 1
"""


def k(a, b):
    if a == b: return 1
    if a < b: return 0
    return k(a - 1, b) + k(a // 2, b)


print(k(50, 20) * k(20, 1))
