import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    paper[y][x] = 0
    c = 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < m:
            if paper[b][a]:
                c += dfs(a, b)
    return c

m, n, k = map(int, input().split())
r = [list(map(int, input().split())) for _ in range(k)]
paper = [[1] * n for _ in range(m)]
for v in r:
    for i in range(v[1], v[3]):
        for j in range(v[0], v[2]):
            paper[i][j] = 0
cnt = []
for i in range(m):
    for j in range(n):
        if paper[i][j]:
            cnt.append(dfs(j, i))
print(len(cnt))
print(*sorted(cnt), sep=' ')