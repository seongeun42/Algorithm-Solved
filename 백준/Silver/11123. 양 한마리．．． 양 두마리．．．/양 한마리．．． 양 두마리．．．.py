import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def dfs(cr, cc, grid, visited):
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if not visited[nr][nc] and grid[nr][nc] == '#':
                visited[nr][nc] = True
                dfs(nr, nc, grid, visited)

def solve():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [input().rstrip() for _ in range(H)]
        ans = 0
        visited = [[False] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if not visited[i][j] and grid[i][j] == '#':
                    visited[i][j] = True
                    dfs(i, j, grid, visited)
                    ans += 1
        print(ans)
    
solve()