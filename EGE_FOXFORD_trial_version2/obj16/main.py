#задание 16
#ans: 3146752
import sys
sys.setrecursionlimit(100000)
def f(n):
    if n == 1:
        return 5
    if n > 1:
        return 2 * n + f(n - 1)
print(f(2048) - f(1024))

#ans: 3146752
dp = [None] * 2100
dp[1] = 5
for n in range(2, len(dp)):
    dp[n] = 2 * n + dp[n - 1]
print(dp[2048] - dp[1024])
