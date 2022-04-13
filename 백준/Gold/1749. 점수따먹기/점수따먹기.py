import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = nums[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
res = -400000001
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(i, N + 1):
            for l in range(j, M + 1):
                res = max(res, dp[k][l] - dp[i - 1][l] - dp[k][j - 1] + dp[i - 1][j - 1])
print(res)