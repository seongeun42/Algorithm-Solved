from collections import deque

def bfs(x, y, visited):
    q = deque([[x, y]])
    visited[y][x] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < C and 0 <= b < R:
                if M[b][a] == 'L' and not visited[b][a]:
                    visited[b][a] = visited[v[1]][v[0]] + 1
                    cnt = max(cnt, visited[b][a])
                    q.append([a, b])
    return cnt - 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
res = 0
for i in range(R):
    for j in range(C):
        if M[i][j] == 'L':
            visited = [[0] * C for _ in range(R)]
            res = max(res, bfs(j, i, visited))
print(res)