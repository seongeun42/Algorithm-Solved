import sys
input = sys.stdin.readline

def dfs(cr, cc, pan, leng, visited):
    if cr == leng - 1 and cc == leng - 1:
        return True
    for d in [(1, 0), (0, 1)]:
        nr, nc = cr + d[0] * pan[cr][cc], cc + d[1] * pan[cr][cc]
        if 0 <= nr < leng and 0 <= nc < leng and not visited[nr][nc]:
            visited[nr][nc] = True
            if dfs(nr, nc, pan, leng, visited):
                return True
    return False

def solve():
    N = int(input())
    pan = [[*map(int, input().split())] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    print("HaruHaru" if dfs(0, 0, pan, N, visited) else "Hing")

solve()