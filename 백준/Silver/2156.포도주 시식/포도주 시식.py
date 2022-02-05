n = int(input())
w = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = w[0]
if n > 1:
    dp[1] = w[0] + w[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i])
print(dp[n-1])