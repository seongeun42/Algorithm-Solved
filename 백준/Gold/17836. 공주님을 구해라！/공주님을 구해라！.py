import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def gram():
    for i in range(N):
        for j in range(M):
            if castle[i][j] == 2:
                return [i, j]

def bfs(s, e, mod):
    q = deque([s])
    visit = [[0] * M for _ in range(N)]
    visit[s[0]][s[1]] = 1
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if [ny, nx] == e:
                return visit[cy][cx]
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx]:
                if mod == 1 or castle[ny][nx] != 1:
                    visit[ny][nx] = visit[cy][cx] + 1
                    q.append([ny, nx])
    return N * M

N, M, T = map(int, input().split())
castle = [[*map(int, input().split())] for _ in range(N)]
g = gram()

hToP = bfs([0, 0], [N - 1, M - 1], 0)
hToG = bfs([0, 0], g, 0)
gToP = bfs(g, [N - 1, M - 1], 1)

ans = min(hToP, hToG + gToP)
print("Fail" if ans > T or ans == N * M else ans)