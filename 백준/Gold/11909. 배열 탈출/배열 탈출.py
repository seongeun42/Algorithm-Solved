import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
dp = [[1e9] * n for _ in range(n)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if i == j == 0: continue
        nxw = dp[i][j - 1] + max(arr[i][j] - arr[i][j - 1] + 1, 0) if 0 < j else 1e9
        nyw = dp[i - 1][j] + max(arr[i][j] - arr[i - 1][j] + 1, 0) if 0 < i else 1e9
        dp[i][j] = min(nxw, nyw)
print(dp[-1][-1])