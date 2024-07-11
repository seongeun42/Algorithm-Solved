import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(cr, cc, visited, num):
    visited[cr][cc] = num
    cnt = 1
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '0' and visited[nr][nc] == -1:
                cnt += dfs(nr, nc, visited, num)
    return cnt

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
cnt = []
visited = [[-1] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0' and visited[i][j] == -1:
            cnt.append(dfs(i, j, visited, len(cnt)))
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            ans[i][j] = 1
            chk = set()
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == '0' and visited[nr][nc] not in chk:
                        ans[i][j] += cnt[visited[nr][nc]]
                        chk.add(visited[nr][nc])
            ans[i][j] %= 10
for v in ans:
    print("".join(map(str, v)))