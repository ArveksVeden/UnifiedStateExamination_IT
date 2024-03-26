"""
+2
*2
*3
2 -> 6 -> 28
"""


def k(a, b):
    if a == b: return 1
    if a > b: return 0
    return k(a + 2, b) + k(a * 2, b) + k(a * 3, b)


print(k(2, 6) * k(6, 28))
