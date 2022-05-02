from _collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    q = deque([[r, c]])
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < M and 0 <= nc < N:
                if plan[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append([nr, nc])
    return 1

M, N = map(int, input().split())
plan = [[*map(int, input().split())] for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, -1, 1, 0, -1, 1, 1, -1]
cnt = 0
for i in range(M):
    for j in range(N):
        if plan[i][j] == 1 and not visited[i][j]:
            cnt += bfs(i, j)
print(cnt)