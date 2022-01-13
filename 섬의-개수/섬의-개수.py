from collections import deque
import sys
input = sys.stdin.readline

def bfs(jd, x, y):
    q = deque([[x, y]])
    jd[y][x] = 0
    while q:
        l = q.popleft()
        dx = [l[0], l[0] + 1, l[0] + 1, l[0] + 1, l[0], l[0] - 1, l[0] - 1, l[0] - 1]
        dy = [l[1] - 1, l[1] - 1, l[1], l[1] + 1, l[1] + 1, l[1] + 1, l[1], l[1] - 1]
        for n in range(8):
            if 0 <= dx[n] < len(jd[0]) and 0 <= dy[n] < len(jd):
                if jd[dy[n]][dx[n]] == 1:
                    jd[dy[n]][dx[n]] = 0
                    q.append([dx[n], dy[n]])
    return 1

while 1:
    n, m = map(int, input().split())
    if n == m == 0: break
    jido = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if jido[i][j] == 1:
                cnt += bfs(jido, j, i)
    print(cnt)
