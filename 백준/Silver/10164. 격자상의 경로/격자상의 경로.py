def dfs(x, y, deX, deY):
    if x == deX and y == deY:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(2):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a <= deX and 0 <= b <= deY:
            dp[y][x] += dfs(a, b, deX, deY)
    return dp[y][x]

N, M, K = map(int, input().split())
k = [(K - 1) // M, (K - 1) % M] if K else [0, 0]
jido = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        jido[i][j] = i * M + j + 1
dp = [[-1] * M for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
if k != [0, 0]:
    print(dfs(0, 0, k[1], k[0]) * dfs(k[1], k[0], M - 1, N - 1))
else:
    print(dfs(0, 0, M - 1, N - 1))