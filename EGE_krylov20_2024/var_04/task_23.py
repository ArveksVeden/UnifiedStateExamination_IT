"""
+2
+3
*5

1 -> 6 -> 35
[21]
"""
from functools import lru_cache


@lru_cache(None)
def k(a, b):
    if a == b: return 1
    if a > b or a == 21: return 0
    return k(a + 2, b) + k(a + 3, b) + k(a * 5, b)


print(k(1, 6) * k(6, 35))
