from collections import deque
import sys
input = sys.stdin.readline

def block(arr, visited, sr, sc):
    q = deque([(sr, sc)])
    leng = len(arr)
    target = arr[sr][sc]
    visited[sr][sc] = target
    total = 1
    rainbow = []
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < leng and 0 <= nc < leng:
                if arr[nr][nc] in [target, 0] and not visited[nr][nc]:
                    if arr[nr][nc] == 0:
                        rainbow.append((nr, nc))
                    visited[nr][nc] = True
                    total += 1
                    q.append((nr, nc))
    for r, c in rainbow:
        visited[r][c] = False
    return total, len(rainbow)

def erase(arr, sr, sc):
    q = deque([(sr, sc)])
    leng = len(arr)
    num = arr[sr][sc]
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < leng and 0 <= nc < leng:
                if arr[nr][nc] == num or arr[nr][nc] == 0:
                    arr[nr][nc] = -2
                    q.append((nr, nc))

def rotate(arr):
    N = len(arr)
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[N - 1 - j][i] = arr[i][j]
    return new_arr

def gravity(arr):
    N = len(arr)
    for c in range(N):
        wall_row = N - 1
        line = [-2] * N
        temp = []
        for r in range(N - 1, -1, -1):
            if arr[r][c] == -1:
                for i, v in enumerate(temp):
                    line[wall_row - i] = v
                temp = [-1]
                wall_row = r
            elif arr[r][c] >= 0:
                temp.append(arr[r][c])
        for i, v in enumerate(temp):
            line[wall_row - i] = v
        for i, v in enumerate(line):
            arr[i][c] = v

def solve():
    N, M = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    score = 0
    while 1:
        largest_block = [0, 0, 0, 0]
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] >= 1 and not visited[i][j]:
                    block_cnt, rainbow_cnt = block(arr, visited, i, j)
                    if block_cnt < 2:
                        continue
                    if largest_block[2] < block_cnt:
                        largest_block = [i, j, block_cnt, rainbow_cnt]
                    elif largest_block[2] == block_cnt and largest_block[3] <= rainbow_cnt:
                            largest_block = [i, j, block_cnt, rainbow_cnt]
        if largest_block == [0, 0, 0, 0]:
            break
        score += largest_block[2] ** 2
        erase(arr, largest_block[0], largest_block[1])
        gravity(arr)
        arr = rotate(arr)
        gravity(arr)
    print(score)

solve()