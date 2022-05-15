def dfs(r, c, dep, s):
    if dep == 6:
        ans.add(s)
        return
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, dep + 1, s + str(pan[nr][nc]))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
pan = [[*map(int, input().split())] for _ in range(5)]
ans = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, 1, str(pan[i][j]))
print(len(ans))