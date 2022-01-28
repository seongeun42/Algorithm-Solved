from collections import deque

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < m and 0 <= b < n:
                if tmt[b][a] == 0:
                    tmt[b][a] = tmt[v[1]][v[0]] + 1
                    q.append([a, b])

def tomato():
    res = 0
    for i in range(n):
        for j in range(m):
            if tmt[i][j] == 0:
                return -1
            res = max(res, tmt[i][j])
    return res - 1

m, n = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 1:
            q.append([j, i])
bfs()
print(tomato())