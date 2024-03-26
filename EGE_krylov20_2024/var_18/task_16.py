dp = [None] * 150
dp[1] = 1
dp[2] = 2

for n in range(3, len(dp)):
    dp[n] = n * (n - 1) * dp[n - 1]

print(dp[123] / dp[120])
