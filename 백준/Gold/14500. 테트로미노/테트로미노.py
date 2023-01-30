import sys
input = sys.stdin.readline

def dfs(r, c, dep, total):
    global res
    if total + max_val * (3 - dep) <= res:
        return
    if dep == 3:
        res = max(res, total)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                if dep == 1:
                    dfs(r, c, dep + 1, total + P[nr][nc])
                dfs(nr, nc, dep + 1, total + P[nr][nc])
                visited[nr][nc] = 0

N, M = map(int, input().split())
P = [[*map(int, input().split())] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [1, 0, 1, 0]
dc = [0, 1, 0, -1]
res = 0
max_val = max(map(max, P))
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 0, P[r][c])
        visited[r][c] = 0
print(res)