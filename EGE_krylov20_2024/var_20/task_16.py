dp = [None] * 100
dp[1] = 1
dp[2] = 2

for n in range(3, len(dp)):
    if n % 2 == 0:
        dp[n] = 3 + dp[n - 1]
    else:
        dp[n] = 2*n + dp[n - 2]
print(dp[42])
