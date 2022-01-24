from collections import deque
import sys
input = sys.stdin.readline

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

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * max(max(m))
cnt[0] = 1
for i in range(len(cnt) - 1, 0, -1):
    for r in range(n):
        for c in range(n):
            if m[r][c] > i:
                bfs(m, c, r, i)
                cnt[i] += 1
print(max(cnt))