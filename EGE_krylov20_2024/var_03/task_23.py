"""
+2
+3
*5
1-> 31
[6, 17]
"""
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)


@lru_cache(None)
def k(a, b):
    if a == b: return 1
    if a > b or a == 6 or a == 17: return 0
    return k(a + 2, b) + k(a + 3, b) + k(a*5, b)


print(k(1, 31))
