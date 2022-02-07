from collections import deque

def bfs():
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, -1, 0, -1, 1, 0, 1, -1]
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(8):
            x, y = v[0] + dx[i], v[1] + dy[i]
            if 0 <= x < m and 0 <= y < n:
                if not jido[y][x]:
                    jido[y][x] = jido[v[1]][v[0]] + 1
                    cnt = max(cnt, jido[y][x])
                    q.append([x, y])
    return cnt

n, m = map(int, input().split())
jido = [[*map(int, input().split())] for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if jido[i][j] == 1:
            q.append([j, i])
print(bfs() - 1)