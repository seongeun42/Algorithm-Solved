import sys
input = sys.stdin.readline

dp = [[0] + [1] * 30]
dp += [[0] * 31 for _ in range(30)]
for i in range(1, 31):
    for j in range(i, 31):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while 1:
    N = int(input())
    if not N:
        break
    print(dp[N][N])