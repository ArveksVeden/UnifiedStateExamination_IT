"""
+3
+4
*3

1 -> 7 -> 30
"""


def k(a, b):
    if a == b: return 1
    if a > b: return 0
    return k(a + 3, b) + k(a + 4, b) + k(a * 3, b)


print(k(1, 7) * k(7, 30))