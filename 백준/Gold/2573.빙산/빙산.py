from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < M and 0 <= b < N and not visited[b][a]:
            if maps[b][a]:
                dfs(a, b)
            else:
                if maps[y][x] > 0:
                    maps[y][x] -= 1

def bfs(x, y):
    q = deque([[x, y]])
    visited[y][x] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < M and 0 <= b < N and not visited[b][a]:
                if maps[b][a]:
                    visited[b][a] = 1
                    q.append([a, b])
                else:
                    if maps[v[1]][v[0]] > 0:
                        maps[v[1]][v[0]] -= 1

N, M = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maps = [[*map(int, input().split())] for _ in range(N)]
res = 0
while 1:
    visited = [[0] * M for _ in range(N)]
    two = 0
    over = 0
    allZero = 1
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maps[i][j] and not visited[i][j]:
                allZero = 0
                if two:
                    over = 1
                    break
                bfs(j, i)
                two = 1
    if allZero or over:
        break
    res += 1
print(res if over else 0)