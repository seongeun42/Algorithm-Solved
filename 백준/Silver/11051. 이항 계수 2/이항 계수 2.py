N, K = map(int, input().split())
dp = [1]
for i in range(1, 1001):
    dp.append(dp[i - 1] * i)
print((dp[N] // (dp[K] * dp[N - K])) % 10007)