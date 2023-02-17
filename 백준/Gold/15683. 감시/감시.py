import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] < 6:
            cctv.append([room[i][j], i, j])

# 북동남서 0123
mode = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 3], [1, 2, 3], [0, 1, 2], [0, 2, 3]],
        [[0, 1, 2, 3]]]

# 북동남서
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

def fill(arr, directs, r, c):
    for d in directs:
        nr, nc = r, c
        while 1:
            nr += dr[d]
            nc += dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                break
            if arr[nr][nc] == 6:
                break
            if arr[nr][nc] == 0:
                arr[nr][nc] = 7

def dfs(dep, arr):
    global ans
    if dep == len(cctv):
        ans = min(ans, sum([l.count(0) for l in arr]))
        return
    tmp = copy.deepcopy(arr)
    cctvNum, r, c = cctv[dep]
    for m in mode[cctvNum]:
        fill(tmp, m, r, c)
        dfs(dep + 1, tmp)
        tmp = copy.deepcopy(arr)

ans = 64
dfs(0, room)
print(ans)