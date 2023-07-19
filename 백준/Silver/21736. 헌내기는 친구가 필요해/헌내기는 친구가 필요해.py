from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def location():
    for i in range(n):
        for j in range(m):
            if camp[i][j] == "I":
                return (i, j)

def bfs(l):
    q = deque([l])
    visited[l[0]][l[1]] = 1
    cnt = 0
    while q:
        cy, cx = q.popleft()
        if camp[cy][cx] == "P":
            cnt += 1
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if camp[ny][nx] != "X":
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    return cnt

n, m = map(int, input().split())
camp = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = bfs(location())
print(cnt if cnt else "TT")