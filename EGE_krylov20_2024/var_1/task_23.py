"""
+1
+4
*2
"""


def k(a, b):
    if a == b: return 1
    if a > b or a == 11 or a == 17: return False
    return k(a + 1, b) + k(a + 4, b) + k(a * 2, b)


print(k(3, 24))