from collections import deque
import sys
input = sys.stdin.readline

def bfs(jd, x, y):
    q = deque([[x, y]])
    while q:
        l = q.popleft()
        dx = [l[0], l[0] + 1, l[0], l[0] - 1]
        dy = [l[1] + 1, l[1], l[1] - 1, l[1]]
        for i in range(4):
            if 0 <= dx[i] < len(jd[0]) and 0 <= dy[i] < len(jd):
                if jd[dy[i]][dx[i]] == 1:
                    q.append([dx[i], dy[i]])
                    jd[dy[i]][dx[i]] = jd[l[1]][l[0]] + 1

n, m = map(int, input().split())
jido = [list(map(int, list(input().strip()))) for _ in range(n)]
bfs(jido, 0, 0)
print(jido[n - 1][m - 1])