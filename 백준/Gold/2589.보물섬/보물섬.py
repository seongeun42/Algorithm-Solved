from collections import deque

def bfs(x, y):
    q = deque([[x, y]])
    c = []
    M[y][x] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < C and 0 <= b < R:
                if M[b][a] == 'L':
                    M[b][a] = M[v[1]][v[0]] + 1
                    cnt = max(cnt, M[b][a])
                    q.append([a, b])
                    c.append([a, b])
    return find(c, cnt)

def find(land, v):
    turn = 0
    cnt = v
    for l in land:
        q = deque([[l[0], l[1]]])
        M[l[1]][l[0]] = -1 if turn % 2 else 1
        while q:
            v = q.popleft()
            for i in range(4):
                a, b = v[0] + dx[i], v[1] + dy[i]
                if 0 <= a < C and 0 <= b < R and M[b][a] != 'W':
                    if turn % 2 and M[b][a] > 0:
                        M[b][a] = M[v[1]][v[0]] - 1
                        cnt = max(cnt, abs(M[b][a]))
                        q.append([a, b])
                    elif turn % 2 == 0 and M[b][a] < 0:
                        M[b][a] = M[v[1]][v[0]] + 1
                        cnt = max(cnt, M[b][a])
                        q.append([a, b])
        turn += 1
    return cnt - 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
res = 0
for i in range(R):
    for j in range(C):
        if M[i][j] == 'L':
            res = max(res, bfs(j, i))
print(res)