import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

def dfs(x, y, visited, union):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    union.append([x, y])
    visited[y][x] = 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < N:
            if L <= abs(A[y][x] - A[b][a]) <= R and not visited[b][a]:
                cnt += dfs(a, b, visited, union)
    return cnt + A[y][x]

N, L, R = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
move, res = [], 0
while 1:
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                tmp = dfs(j, i, visited, union)
                if tmp != A[i][j]:
                    move.append([tmp//len(union), union])
    if move:
        res += 1
        while move:
            k = move.pop()
            for xy in k[1]:
                A[xy[1]][xy[0]] = k[0]
    else:
        break
print(res)