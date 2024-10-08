from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    hx, hy = map(int, input().split())
    ex, ey = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = deque([(hx - 1, hy - 1, 0)])
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][hx - 1][hy - 1] = 0
    while q:
        cr, cc, broken = q.popleft()
        if cr == ex - 1 and cc == ey - 1:
            print(visited[broken][cr][cc])
            return
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and not visited[broken][nr][nc]:
                    visited[broken][nr][nc] = visited[broken][cr][cc] + 1
                    q.append((nr, nc, broken))
                elif arr[nr][nc] == 1 and not broken:
                    visited[1][nr][nc] = visited[0][cr][cc] + 1
                    q.append((nr, nc, 1))
    print(-1)

solve()