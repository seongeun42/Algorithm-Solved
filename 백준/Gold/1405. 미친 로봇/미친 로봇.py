def dfs(cx, cy, dep, per):
    global ans
    if dep == N:
        ans += per
        return
    for i in range(4):
        if s[i + 1] == 0:
            continue
        nx = cx + dx[i]
        ny = cy + dy[i]
        if visit[ny][nx] == 1:
            continue
        visit[ny][nx] = 1
        dfs(nx, ny, dep + 1, per * (s[i + 1] / 100))
        visit[ny][nx] = 0

s = [*map(int, input().split())]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = s[0]
ans = 0
visit = [[0] * 29 for _ in range(29)]
visit[14][14] = 1
dfs(14, 14, 0, 1)
print(ans)