import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(p, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    c = p[y][x]
    p[y][x] = 0
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < n and 0 <= b < n:
            if p[b][a] == c:
                dfs(p, a, b)
    return 1

n = int(input())
pic = [list(input().strip()) for _ in range(n)]
pic_p = []
for l in pic:
    pic_p.append([])
    for v in l:
        pic_p[-1].append('R' if v == 'G' else v)
cnt, cnt_p = 0, 0
for i in range(n):
    for j in range(n):
        if pic[i][j] != 0:
            cnt += dfs(pic, j, i)
        if pic_p[i][j] != 0:
            cnt_p += dfs(pic_p, j, i)
print(cnt, cnt_p, sep=' ')