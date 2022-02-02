from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[x, y]])
    w, s = 0, 0
    if md[y][x] == 'v': w += 1
    elif md[y][x] == 'o': s += 1
    md[y][x] = 0
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < C and 0 <= b < R:
                if md[b][a] != '#' and md[b][a] != 0:
                    if md[b][a] == 'v':
                        w += 1
                    elif md[b][a] == 'o':
                        s += 1
                    md[b][a] = 0
                    q.append([a, b])
    return [s, 0] if s > w else [0, w]



R, C = map(int, input().split())
md = [list(input()) for _ in range(R)]
ws = [0, 0]
for i in range(R):
    for j in range(C):
        if md[i][j] != '#' and md[i][j] != 0:
            cnt = bfs(j, i)
            ws[0] += cnt[0]
            ws[1] += cnt[1]
print(*ws)