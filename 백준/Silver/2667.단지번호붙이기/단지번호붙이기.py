from collections import deque

def dfs(jib, x, y):
    jib[y][x], c = 0, 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        l, m = x + dx[k], y + dy[k]
        if 0 <= l < len(jib) and 0 <= m < len(jib):
            if jib[m][l]:
                c += dfs(jib, l, m)
    return c

def bfs(jib, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    jib[y][x], c = 0, 1
    q = deque([[x, y]])
    while q:
        v = q.popleft()
        for k in range(4):
            l, m = v[0] + dx[k], v[1] + dy[k]
            if 0 <= l < len(jib) and 0 <= m < len(jib):
                if jib[m][l]:
                    jib[m][l] = 0
                    q.append([l, m])
                    c += 1
    return c

n = int(input())
jib = [list(map(int, input())) for _ in range(n)]
cnt = []
for i in range(n):
    for j in range(n):
        if jib[i][j] == 1:
            cnt.append(dfs(jib, j, i))
            # cnt.append(bfs(jib, j, i))
cnt.sort()
print(len(cnt), *cnt, sep='\n')
