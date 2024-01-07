import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(cy, cx):
    cnt = [1] * 4
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and forest[ny][nx] > forest[cy][cx]:
            cnt[i] += dfs(ny, nx) if dp[ny][nx] == 0 else dp[ny][nx]
    dp[cy][cx] = max(cnt)
    return dp[cy][cx]

n = int(input())
forest = [[*map(int, input().split())] for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dfs(i, j)
print(max(map(max, dp)))