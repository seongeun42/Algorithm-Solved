import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(cr, cc, arr, visited):
    visited[cr][cc] = True
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < len(arr) and 0 <= nc < len(arr[0]):
            if not visited[nr][nc] and arr[nr][nc] == 255:
                dfs(nr, nc, arr, visited)

def solve():
    N, M = map(int, input().split())
    RGB = [[*map(int, input().split())] for _ in range(N)]
    T = int(input())
    arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(0, M * 3, 3):
            arr[i].append(255 if sum(RGB[i][j:j+3]) // 3 >= T else 0)
    ans = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 255 and not visited[i][j]:
                ans +=1
                dfs(i, j, arr, visited)
    print(ans)

solve()