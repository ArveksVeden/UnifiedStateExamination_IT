dp = [None] * 2100
dp[1] = 1
dp[2] = 2

for n in range(3, len(dp)):
    dp[n] = n * (n - 1) + dp[n - 1] - dp[n - 2]

print(dp[2024] + dp[2020] - dp[2019])
