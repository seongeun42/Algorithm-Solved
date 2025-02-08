from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    pan = [[*map(int, input().split())] for _ in range(N)]
    psum = [[0] * (M + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            psum[r][c] = pan[r - 1][c - 1] + psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1]
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
            if 0 <= nr < N and 0 <= nc < M and 0 <= nr + H - 1 < N and 0 <= nc + W - 1 < M and visited[nr][nc] == 0:
                check = psum[nr + H][nc + W] - psum[nr][nc + W] - psum[nr + H][nc] + psum[nr][nc]
                if check == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))
    return -1

print(solve())