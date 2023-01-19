dp = [[1] * 10] + [[1] + [0] * 9 for _ in range(64)]
for i in range(1, 65):
    for j in range(1, 10):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

t = int(input())
for _ in range(t):
    print(dp[int(input())][9])