from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maps, n, m):
    q = deque([(0, 0)])
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (ny, nx) == (n - 1, m - 1):
                return visit[y][x] + 1
            if 0 <= ny < n and 0 <= nx < m:
                if not visit[ny][nx] and maps[ny][nx] == 1:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny, nx))
    return -1

def solution(maps):
    return bfs(maps, len(maps), len(maps[0]))