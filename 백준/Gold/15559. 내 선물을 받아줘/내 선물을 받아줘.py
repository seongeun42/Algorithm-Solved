import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
ans = 0

def dfs(cr, cc, jido, visited, cnt):
    global ans
    visited[cr][cc] = cnt
    d = jido[cr][cc]
    nr, nc = cr + direction[d][0], cc + direction[d][1]
    if 0 <= nr < len(visited) and 0 <= nc < len(visited[0]):
        if not visited[nr][nc]:
            dfs(nr, nc, jido, visited, cnt)
        elif visited[nr][nc] == cnt:
            ans += 1

def solve():
    N, M = map(int, input().split())
    jido = [input().rstrip() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                dfs(i, j, jido, visited, cnt)
                cnt += 1
    print(ans)

solve()