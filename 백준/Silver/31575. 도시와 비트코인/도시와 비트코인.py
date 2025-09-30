import sys
input = sys.stdin.readline

def dfs(cr, cc, visited, city, N, M):
    visited[cr][cc] = 1
    if cr == N and cc == M:
        return
    for r, c in [(1, 0), (0, 1)]:
        nr, nc = cr + r, cc + c
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and city[nr][nc]:
            dfs(nr, nc, visited, city, N, M)

def solve():
    N, M = map(int, input().split())
    city = [[*map(int, input().split())] for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    dfs(0, 0, visited, city, N, M)
    print("Yes" if visited[-1][-1] else "No")

solve()