from collections import deque

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]
    while q:
        v = q.popleft()
        for i in range(6):
            a, b, c = v[0] + dh[i], v[1] + dx[i], v[2] + dy[i]
            if 0 <= a < H and 0 <= b < M and 0 <= c < N:
                if box[a][c][b] == 0:
                    box[a][c][b] = box[v[0]][v[2]][v[1]] + 1
                    q.append([a, b, c])

def tmt():
    res = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return -1
                res = max(res, box[h][n][m])
    return res - 1

M, N, H = map(int, input().split())
box = []
q = deque([])
for _ in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])
for h in range(H):
    for n in range(N):
        for m in range(M):
           if box[h][n][m] == 1:
               q.append([h, m, n])
bfs()
print(tmt())