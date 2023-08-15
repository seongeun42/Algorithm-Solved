from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(jd, x, y, h):
    jd[y][x] = h
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < len(m) and 0 <= b < len(m):
            if m[b][a] > h:
                dfs(jd, a, b, h)
    return 1

def bfs(jd, x, y, h):
    jd[y][x] = h
    q = deque([[x, y]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < len(jd) and 0 <= b < len(jd):
                if jd[b][a] > h:
                    jd[b][a] = h
                    q.append([a, b])
    return 1

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
res = 1
for i in range(max(map(max, m)) - 1, 0, -1):
    cnt = 0
    for r in range(n):
        for c in range(n):
            if m[r][c] > i:
                # cnt += dfs(m, c, r, i)
                cnt += bfs(m, c, r, i)
    res = max(res, cnt)
print(res)