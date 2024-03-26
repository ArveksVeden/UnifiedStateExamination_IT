"""
+1
+4
*2
4 -> 11 -> 28
[18]
"""


def k(a, b):
    if a == b:
        return 1
    if a > b or a == 18:
        return False
    return k(a + 1, b) + k(a + 4, b) + k(a * 2, b)


print(k(4, 11) * k(11, 28))
