from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[x, y]])
    pic[y][x] = 0
    cnt = 1
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < m and 0 <= b < n:
                if pic[b][a]:
                    pic[b][a] = 0
                    cnt += 1
                    q.append([a, b])
    return cnt

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
area = []
for i in range(n):
    for j in range(m):
        if pic[i][j]:
            area.append(bfs(j, i))
if area:
    print(len(area), max(area), sep='\n')
else:
    print(0, 0)