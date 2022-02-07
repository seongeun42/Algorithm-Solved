from collections import deque

def bfs(visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[0, 0]])
    visited[0][0] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(4):
            x, y = v[0] + dx[i], v[1] + dy[i]
            if 0 <= x < m and 0 <= y < n and not visited[y][x]:
                visited[y][x] = 1
                if pan[y][x] == 0:
                    q.append([x, y])
                elif pan[y][x] == 1:
                    pan[y][x] = 0
                    cnt += 1
    return cnt

n, m = map(int, input().split())
pan = [[*map(int, input().split())] for _ in range(n)]
time = -1
res = []
while 1:
    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs(visited)
    if cnt == 0:
        break
    else:
        res.append(cnt)
print(time, res[-1], sep='\n')