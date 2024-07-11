import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def count(cr, cc):
    cnt_arr[cr][cc] = -1
    cnt = 1
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '0' and cnt_arr[nr][nc] == 0:
                cnt += count(nr, nc)
    return cnt

def fill(cr, cc, cnt, idx):
    cnt_arr[cr][cc] = (cnt, idx)
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '0' and cnt_arr[nr][nc] == -1:
                fill(nr, nc, cnt, idx)

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
cnt_arr = [[0] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]
idx = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0' and cnt_arr[i][j] == 0:
            fill(i, j, count(i, j), idx)
            idx += 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            ans[i][j] = 1
            chk = set()
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == '0' and cnt_arr[nr][nc][1] not in chk:
                        ans[i][j] += cnt_arr[nr][nc][0]
                        chk.add(cnt_arr[nr][nc][1])
            ans[i][j] %= 10
for v in ans:
    print("".join(map(str, v)))