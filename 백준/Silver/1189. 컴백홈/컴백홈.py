import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
ans = 0

def backtrack(cr, cc, dep, visited, jido, K):
    global ans
    if cr == 0 and cc == len(jido[0]) - 1:
        if dep == K - 1:
            ans += 1
        return
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < len(jido) and 0 <= nc < len(jido[0]):
            if not visited[nr][nc] and jido[nr][nc] != 'T':
                visited[nr][nc] = 1
                backtrack(nr, nc, dep + 1, visited, jido, K)
                visited[nr][nc] = 0

def solve():
    R, C, K = map(int, input().split())
    jido = [input().rstrip() for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    visited[R - 1][0] = 1
    backtrack(R - 1, 0, 0, visited, jido, K)
    print(ans)

solve()