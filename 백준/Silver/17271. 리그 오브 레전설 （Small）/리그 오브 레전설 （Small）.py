N, M = map(int, input().split())
dp = [1] * (N + 1)
for i in range(M, N + 1):
    dp[i] = (dp[i - 1] + dp[i - M]) % 1_000_000_007
print(dp[N])