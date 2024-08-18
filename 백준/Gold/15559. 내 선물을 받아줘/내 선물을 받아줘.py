import sys
input = sys.stdin.readline

direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def dfs(cr, cc, jido, visited, R):
    visited[cr][cc] = 1
    d = jido[cr][cc]
    nr, nc = cr + direction[d][0], cc + direction[d][1]
    if 0 <= nr < len(visited) and 0 <= nc < len(visited[0]):
        c = cr * len(visited[0]) + cc
        n = nr * len(visited[0]) + nc
        croot = find_root(c, R)
        nroot = find_root(n, R)
        if croot != nroot:
            R[max(croot, nroot)] = min(croot, nroot)
        if not visited[nr][nc]:
            dfs(nr, nc, jido, visited, R)

def solve():
    N, M = map(int, input().split())
    jido = [input().rstrip() for _ in range(N)]
    R = [i for i in range(N * M)]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                dfs(i, j, jido, visited, R)
    ans = 0
    for i in range(N * M):
        if R[i] == i:
            ans += 1
    print(ans)

solve()