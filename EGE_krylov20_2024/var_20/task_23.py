"""
+5
+4
*3

2 -> 6 -> 30
"""
import sys
sys.setrecursionlimit(100000)


def k(a, b):
    if a == b: return 1
    if a > b: return 0
    return k(a + 5, b) + k(a + 4, b) + k(a*3, b)


print(k(2, 30))