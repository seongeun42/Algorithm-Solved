n, k = map(int, input().split())
dp = [[], [1], [1, 1]]
for i in range(3, n + 1):
    dp.append([1])
    for j in range(1, i - 1):
        dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
    dp[i].append(1)
print(dp[n][k - 1])