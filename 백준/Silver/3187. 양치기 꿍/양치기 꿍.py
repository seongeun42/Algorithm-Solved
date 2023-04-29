import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sr, sc):
    global s, w
    q = deque([(sr, sc)])
    visit[sr][sc] = 1
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]
            if 0 <= nr < r and 0 <= nc < c:
                if not visit[nr][nc] and area[nr][nc] != "#":
                    if area[nr][nc] == "v":
                        w += 1
                    elif area[nr][nc] == "k":
                        s += 1
                    visit[nr][nc] = 1
                    q.append((nr, nc))

r, c = map(int, input().split())
area = [input() for _ in range(r)]
visit = [[0] * c for _ in range(r)]
sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if not visit[i][j] and area[i][j] != "#":
            s, w = 0, 0
            if area[i][j] == "v":
                w += 1
            elif area[i][j] == "k":
                s += 1
            visit[i][j] = 1
            bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w
print(sheep, wolf)