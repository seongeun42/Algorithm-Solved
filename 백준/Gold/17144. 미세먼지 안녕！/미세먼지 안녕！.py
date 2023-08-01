import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def spread(desc, src):
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if src[i][j] == 0:
                continue
            if src[i][j] == -1:
                desc[i][j] = -1
                continue
            cx, cy = j, i
            cnt = 0
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < C and 0 <= ny < R:
                    if src[ny][nx] == -1:
                        continue
                    if visited[ny][nx] == 0:
                        desc[ny][nx] = src[cy][cx] // 5
                        visited[ny][nx] = 1
                    else:
                        desc[ny][nx] += src[cy][cx] // 5
                    cnt += 1
            v = src[cy][cx] - (src[cy][cx] // 5) * cnt
            if visited[cy][cx] == 0:
                desc[cy][cx] = v
                visited[cy][cx] = 1
            else:
                desc[cy][cx] += v
    return desc

def airUp(r):
    for cr in range(r - 1, 0, -1):
        A[cr][0] = A[cr - 1][0]
    for cc in range(C - 1):
        A[0][cc] = A[0][cc + 1]
    for cr in range(r):
        A[cr][C - 1] = A[cr + 1][C - 1]
    for cc in range(C - 1, 1, -1):
        A[r][cc] = A[r][cc - 1]
    A[r][1] = 0

def airDown(r):
    for cr in range(r + 1, R - 1):
        A[cr][0] = A[cr + 1][0]
    for cc in range(C - 1):
        A[R - 1][cc] = A[R - 1][cc + 1]
    for cr in range(R - 1, r, -1):
        A[cr][C - 1] = A[cr - 1][C - 1]
    for cc in range(C - 1, 1, -1):
        A[r][cc] = A[r][cc - 1]
    A[r][1] = 0

R, C, T = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(R)]
air = []
for i in range(R):
    if A[i][0] == -1:
        air.append(i)
for _ in range(T):
    A = spread([[0] * C for _ in range(R)], A)
    airUp(air[0])
    airDown(air[1])

ans = 2
for i in range(R):
    for j in range(C):
        ans += A[i][j]
print(ans)