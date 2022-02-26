import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(c, r, chr):
    war[r][c] = 0
    cnt = 1
    for i in range(4):
        x, y = c + dx[i], r + dy[i]
        if 0 <= x < N and 0 <= y < M and war[y][x] == chr:
            cnt += dfs(x, y, chr)
    return cnt

N, M = map(int, input().split())
war = [list(input().strip()) for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
w, b = 0, 0
for i in range(M):
    for j in range(N):
        if war[i][j] == 'W':
            v = dfs(j, i, 'W')
            w += v ** 2
        elif war[i][j] == 'B':
            v = dfs(j, i, 'B')
            b += v ** 2
print(w, b)