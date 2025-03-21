from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def iceburg_cnt(arr, sr, sc, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < len(arr) and 0 <= nc < len(arr):
                if not visited[nr][nc] and arr[nr][nc] > 0:
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))
    return cnt


def ice_decrease(new_arr, no_ice, line_cnt):
    cnt = [[0] * line_cnt for _ in range(line_cnt)]
    for i in range(line_cnt):
        cnt[i][0] += 1
        cnt[0][i] += 1
        cnt[i][line_cnt - 1] += 1
        cnt[line_cnt - 1][i] += 1
    decrease_list = {(0, 0), (0, line_cnt - 1), (line_cnt - 1, 0), (line_cnt - 1, line_cnt - 1)}
    for cr, cc in no_ice:
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < line_cnt and 0 <= nc < line_cnt:
                cnt[nr][nc] += 1
                if cnt[nr][nc] > 1:
                    decrease_list.add((nr, nc))
    for r, c in decrease_list:
        if new_arr[r][c] > 0:
            new_arr[r][c] -= 1


def firestorm(arr, sub_cnt, line_cnt):
    new_arr = [[0] * line_cnt for _ in range(line_cnt)]
    no_ice = deque([])
    for sr in range(0, line_cnt, sub_cnt):
        for sc in range(0, line_cnt, sub_cnt):
            for i in range(sr, sr + sub_cnt):
                for j in range(sc, sc + sub_cnt):
                    new_arr[j - sc + sr][sub_cnt - 1 - i + sr + sc] = arr[i][j]
                    if arr[i][j] == 0:
                        no_ice.append((j - sc + sr, sub_cnt - 1 - i + sr + sc))
    ice_decrease(new_arr, no_ice, line_cnt)
    return new_arr


def solve():
    N, Q = map(int, input().split())
    line_cnt = 2 ** N
    A = [[*map(int, input().split())] for _ in range(line_cnt)]
    L = [*map(int, input().split())]
    for l in L:
        A = firestorm(A, 2 ** l, line_cnt)
    total = 0
    biggest_ice = 0
    visited = [[False] * line_cnt for _ in range(line_cnt)]
    for i in range(line_cnt):
        for j in range(line_cnt):
            total += A[i][j]
            if not visited[i][j] and A[i][j] > 0:
                cnt = iceburg_cnt(A, i, j, visited)
                if biggest_ice < cnt:
                    biggest_ice = cnt
    print(total, biggest_ice, sep="\n")

solve()