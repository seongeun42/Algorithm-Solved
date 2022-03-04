from _collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def check(visit):
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                return 0
    return 1

def bfs(Q, visit):
    cnt = 0
    for x, y in Q:
        visit[y][x] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < N and 0 <= b < N and not visit[b][a]:
                visit[b][a] = visit[y][x] + 1
                Q.append([a, b])
                if lap[b][a] != 2:
                    cnt = max(cnt, visit[b][a])
    return cnt - 1 if check(visit) else 1e9

N, M = map(int, input().split())
lap = [[*map(int, input().split())] for _ in range(N)]
V = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
existZero = 0
for i in range(N):
    for j in range(N):
        if lap[i][j] == 2:
            V.append([j, i])
        if lap[i][j] == 0:
            existZero = 1
if existZero:
    res = 1e9
    for v in list(combinations(V, M)):
        q = deque(v)
        visited = []
        for i in range(N):
            visited.append([])
            for j in range(N):
                if lap[i][j] == 1:
                    visited[i].append(-1)
                else:
                    visited[i].append(0)
        res = min(res, bfs(q, visited))
    print(res if res != 1e9 else -1)
else:
    print(0)