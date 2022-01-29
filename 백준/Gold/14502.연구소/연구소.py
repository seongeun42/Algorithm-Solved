from collections import deque
from itertools import combinations
import copy

def bfs(w):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tmp = copy.deepcopy(lab)
    q = deque(virus)
    for i in range(3):
        tmp[w[i][1]][w[i][0]] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < M and 0 <= b < N:
                if tmp[b][a] == 0:
                    tmp[b][a] = 2
                    q.append([a, b])
    return cnt_safe(tmp)

def cnt_safe(tmp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
zero, virus = [], []
for n in range(N):
    for m in range(M):
        if lab[n][m] == 2:
            virus.append([m, n])
        elif lab[n][m] == 0:
            zero.append([m, n])
wall = list(combinations(zero, 3))
res = 0
for w in wall:
    res = max(res, bfs(w))
print(res)