from collections import deque

def bfs():
    q = deque([[0, 7, 0]])
    visit[7][0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if cnt >= 8:
            return 1
        if [x, y] == [7, 0]:
            return 1
        if pan[y][x] != '#':
            for i in range(9):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not visit[ny][nx][cnt + 1] and pan[ny][nx] != '#':
                        visit[ny][nx][cnt + 1] = 1
                        q.append([nx, ny, cnt + 1])
        if wall and q and cnt + 1 == q[0][2]:
            size = len(wall)
            for i in range(size):
                wx, wy = wall.popleft()
                if wy + 1 < 8:
                    pan[wy + 1][wx] = '#'
                    wall.append([wx, wy + 1])
                pan[wy][wx] = '.'
    return 0

pan = [list(input()) for _ in range(8)]
visit = [[[0] * 9 for _ in range(8)] for _ in range(8)]
wall = []
for i in range(8):
    for j in range(8):
        if pan[i][j] == '#':
            wall.append([j, i])
wall = deque(sorted(wall, key=lambda x: -x[1]))
dx = [0, 1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, 1, -1, 1, -1, 1, -1]
print(bfs())