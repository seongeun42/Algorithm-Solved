from collections import deque

def bfs():
    q = deque([[0, 0, C]])
    while q:
        a, b, c = q.pop()
        if visited[a][b] == 1: continue
        if a == 0:
            res.add(c)
        visited[a][b] = 1
        if a + c > A: q.append([A, b, c + a - A])
        else: q.append([a + c, b, 0])
        if b + c > B: q.append([a, B, c + b - B])
        else: q.append([a, b + c, 0])
        if b + a > B: q.append([a + b - B, B, c])
        else: q.append([0, a + b, c])
        if c + a > C: q.append([a + c - C, b, C])
        else: q.append([0, b, c + a])
        if a + b > A: q.append([A, b + a - A, c])
        else: q.append([a + b, 0, c])
        if c + b > C: q.append([a, b + c - C, C])
        else: q.append([a, 0, c + b])

A, B, C = map(int, input().split())
visited = [[0] * (B + 1) for _ in range(A + 1)]
res = set()
bfs()
print(*sorted(list(res)), sep=' ')