import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(newC):
    global cnt
    q = deque([(0, 0)])
    visit[0][0] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if cheese[ny][nx] == 0 and not visit[ny][nx]:
                    q.append((nx, ny))
                visit[ny][nx] += 1
                if newC[ny][nx] == 1 and cheese[ny][nx] == 1 and visit[ny][nx] >= 2:
                    newC[ny][nx] = 0
                    cnt -= 1
    return newC

n, m = map(int, input().split())
cheese = [[*map(int, input().split())] for _ in range(n)]
cnt = sum(map(sum, cheese))
i = 0
while cnt > 0:
    visit = [[0] * m for _ in range(n)]
    cheese = bfs(copy.deepcopy(cheese))
    i += 1
print(i)