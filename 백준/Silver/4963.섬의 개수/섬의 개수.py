from collections import deque
import sys
input = sys.stdin.readline

def bfs(jd, x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    q = deque([[x, y]])
    jd[y][x] = 0
    while q:
        l = q.popleft()
        for n in range(8):
            if l[0] + dx[n] >= 0 and l[0] + dx[n] < len(jd[0]):
                if l[1] + dy[n] >= 0 and l[1] + dy[n] < len(jd):
                    if jd[l[1] + dy[n]][l[0] + dx[n]] == 1:
                        jd[l[1] + dy[n]][l[0] + dx[n]] = 0
                        q.append([l[0] + dx[n], l[1] + dy[n]])
    return 1

n, m = map(int, input().split())
while n != 0 or m != 0:
    jido = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if jido[i][j] == 1:
                cnt += bfs(jido, j, i)
    print(cnt)
    n, m = map(int, input().split())