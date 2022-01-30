import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def fire():
    global f
    for _ in range(len(f)):
        x, y = f.popleft()
        for a, b in dir:
            nx = x + a
            ny = y + b
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != '#' and s[nx][ny] != 'F':
                s[nx][ny] = 'F'
                f.append((nx, ny))


def bfs():

    q = deque()
    q.append([(sx, sy), 0])
    visit = [[False] * w for _ in range(h)]
    visit[sx][sy] = True
    tmp = -1

    while q:
        x, cnt = q.popleft()
        #층이 바뀔때만 불을 번짐
        if tmp < cnt:
            tmp = cnt
            fire()

        for a, b in dir:
            nx = x[0] + a
            ny = x[1] + b

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                return cnt + 1

            if not visit[nx][ny] and s[nx][ny] == '.':
                q.append([(nx, ny), cnt + 1])
                visit[nx][ny] = True

    return 'IMPOSSIBLE'


h, w = map(int, input().split())
s = []
f = deque([])

for i in range(h):
    s.append(list(map(str, input().strip())))

for i in range(h):
    for j in range(w):
        if s[i][j] == 'F':
            f.append((i, j))
        elif s[i][j] == 'J':
            sx, sy = i, j
            
print(bfs())