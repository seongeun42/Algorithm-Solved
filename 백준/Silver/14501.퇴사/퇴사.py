n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if tp[i][0] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], tp[i][1] + dp[i + tp[i][0]])
print(dp[0])