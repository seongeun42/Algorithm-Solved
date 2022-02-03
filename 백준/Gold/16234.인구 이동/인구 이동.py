from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([[x, y]])
    cnt = A[y][x]
    union = [[x, y]]
    visited[y][x] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            a, b = v[0] + dx[i], v[1] + dy[i]
            if 0 <= a < N and 0 <= b < N:
                if L <= abs(A[v[1]][v[0]] - A[b][a]) <= R and not visited[b][a]:
                    cnt += A[b][a]
                    visited[b][a] = 1
                    union.append([a, b])
                    q.append([a, b])
    return [cnt // len(union), union] if cnt != A[y][x] else 0

N, L, R = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
move, res = [], 0
while 1:
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tmp = bfs(j, i, visited)
                if tmp:
                    move.append(tmp)
    if move:
        res += 1
        while move:
            k = move.pop()
            for xy in k[1]:
                A[xy[1]][xy[0]] = k[0]
    else:
        break
print(res)