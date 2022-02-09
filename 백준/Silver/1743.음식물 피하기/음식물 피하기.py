import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(r, c):
    mp[r][c] = 0
    cnt = 1
    for i in range(4):
        x, y = c + dx[i], r + dy[i]
        if 0 <= x < M and 0 <= y < N:
            if mp[y][x] == 1:
                cnt += dfs(y, x)
    return cnt

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M, K = map(int, input().split())
mp = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    mp[r-1][c-1] = 1
res = []
for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            res.append(dfs(i, j))
print(max(res))