from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, M, home, start, end, stuff):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    visited = [[[0] * (2 ** len(stuff)) for _ in range(N)] for _ in range(M)]
    visited[start[0]][start[1]][0] = 1
    q = deque([(*start, 0)])
    while q:
        cr, cc, cstuff = q.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < M and 0 <= nc < N and home[nr][nc] != '#' and not visited[nr][nc][cstuff]:
                nstuff = cstuff
                if home[nr][nc] == 'X':
                    nstuff = cstuff | (1 << stuff[(nr, nc)])
                if home[nr][nc] == 'E' and nstuff == (2 ** len(stuff) - 1):
                    return visited[cr][cc][cstuff]
                visited[nr][nc][nstuff] = visited[cr][cc][cstuff] + 1
                q.append((nr, nc, nstuff))

def solve():
    N, M = map(int, input().split())
    home = [input().rstrip() for _ in range(M)]
    start, end = None, None
    stuff = {}
    for i in range(M):
        for j in range(N):
            if home[i][j] == 'X':
                stuff[(i, j)] = len(stuff)
            elif home[i][j] == 'S':
                start = (i, j)
            elif home[i][j] == 'E':
                end = (i, j)
    print(bfs(N, M, home, start, end, stuff))

solve()