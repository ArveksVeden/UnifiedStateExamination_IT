import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 4
    if n > 1:
        return 3 * n + f(n - 1)
print(f(1049) - f(1023))

//////

dp = [None] * 1100
dp[1] = 4
for n in range(2, len(dp)):
    dp[n] = n * 3 + dp[n - 1]
print(dp[1049] - dp[1023])
