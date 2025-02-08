from collections import deque
import sys
input = sys.stdin.readline

def check(r, c, d, pan, H, W):
    if d in {0, 1}:
        for cc in range(c, c + W):
            cr = r if d == 0 else r + H - 1
            if pan[cr][cc] == 1:
                return False
    else:
        for cr in range(r, r + H):
            cc = c if d == 2 else c + W - 1
            if pan[cr][cc] == 1:
                return False
    return True

def solve():
    N, M = map(int, input().split())
    pan = [[*map(int, input().split())] for _ in range(N)]
    H, W, Sr, Sc, Fr, Fc = map(int, input().split())
    visited = [[0] * M for _ in range(N)]
    visited[Sr - 1][Sc - 1] = 1
    q = deque([(Sr - 1, Sc - 1)])
    dc = [0, 0, -1, 1]
    dr = [-1, 1, 0, 0]
    while q:
        cr, cc = q.popleft()
        if (cr, cc) == (Fr - 1, Fc - 1):
            return visited[cr][cc] - 1
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nr + H - 1 < N and 0 <= nc + W - 1 < M:
                if visited[nr][nc] == 0 and check(nr, nc, d, pan, H, W):
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))
    return -1

print(solve())