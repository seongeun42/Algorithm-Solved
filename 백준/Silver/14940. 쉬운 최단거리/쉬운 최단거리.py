import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sy][sx] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
                if jido[ny][nx]:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
jido = [[0] * m for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    l = [*map(int, input().split())]
    for j in range(m):
        jido[i][j] = l[j]
        if l[j] == 2:
            sx, sy = j, i

visited = [[-1] * m for _ in range(n)]
bfs(sx, sy)

for i in range(n):
    for j in range(m):
        if jido[i][j] == 0:
            visited[i][j] = 0

for l in visited:
    print(*l)