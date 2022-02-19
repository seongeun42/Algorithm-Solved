def dfs(a, b, c):
    if visited[a][b] == 1:
        return
    visited[a][b] = 1
    if a == 0:
        res.append(c)
    if a + c > A: dfs(A, b, c + a - A)
    else: dfs(a + c, b, 0)
    if b + c > B: dfs(a, B, c + b - B)
    else: dfs(a, b + c, 0)
    if b + a > B: dfs(a + b - B, B, c)
    else: dfs(0, a + b, c)
    if c + a > C: dfs(a + c - C, b, C)
    else: dfs(0, b, c + a)
    if a + b > A: dfs(A, b + a - A, c)
    else: dfs(a + b, 0, c)
    if c + b > C: dfs(a, b + c - C, C)
    else: dfs(a, 0, c + b)
        
A, B, C = map(int, input().split())
visited = [[0] * (B + 1) for _ in range(A + 1)]
res = []
dfs(0, 0, C)
print(*sorted(res))