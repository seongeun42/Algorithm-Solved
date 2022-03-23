import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < M:
            if jido[b][a] < jido[y][x]:
                dp[y][x] += dfs(a, b)
    return dp[y][x]

M, N = map(int, input().split())
jido = [[*map(int, input().split())] for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0, 0))