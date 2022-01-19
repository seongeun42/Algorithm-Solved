def dfs(jib, x, y):
    jib[y][x], c = 0, 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        l, m = x + dx[i], y + dy[i]
        if l >= 0 and l < len(jib) and m >= 0 and m < len(jib):
            if jib[m][l]:
                c += dfs(jib, l, m)
    return c

n = int(input())
jib = [list(map(int, input())) for _ in range(n)]
cnt = []
for i in range(n):
    for j in range(n):
        if jib[i][j] == 1:
            cnt.append(dfs(jib, j, i))
cnt.sort()
print(len(cnt), *cnt, sep='\n')