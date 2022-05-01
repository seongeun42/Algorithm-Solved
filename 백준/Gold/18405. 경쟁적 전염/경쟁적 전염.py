from _collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while virus:
        v, c, r, s = virus.popleft()
        if s == S:
            break
        for i in range(4):
            nc, nr = c + dx[i], r + dy[i]
            if 0 <= nc < N and 0 <= nr < N and not lab[nr][nc]:
                lab[nr][nc] = v
                virus.append((v, nc, nr, s + 1))
    return lab[R - 1][C - 1]

N, K = map(int, input().split())
lab = [[*map(int, input().split())] for _ in range(N)]
S, R, C = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] != 0:
            virus.append((lab[i][j], j, i, 0))
virus.sort()
virus = deque(virus)
print(bfs())