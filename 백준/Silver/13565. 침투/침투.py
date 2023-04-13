import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visit[y][x] = 1
    if y == M - 1:
        return True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visit[ny][nx] and pan[ny][nx] == "0":
                if dfs(nx, ny):
                    return True
    return False

M, N = map(int, input().split())
pan = [input().strip() for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visit = [[0] * N for _ in range(M)]
ans = False
for i in range(N):
    if not visit[0][i] and pan[0][i] == "0":
        ans = dfs(i, 0)
        if ans:
            break
print("YES" if ans else "NO")