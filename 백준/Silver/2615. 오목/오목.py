import sys
input = sys.stdin.readline

def count(mr, mc, sr, sc, al):
    cnt = 0
    while 0 <= sr < 19 and 0 <= sc < 19 and pan[sr][sc] == al:
        cnt += 1
        sr += mr
        sc += mc
    return cnt

def check(d, row, col, al):
    cnt = count(dr[d], dc[d], row + dr[d], col + dc[d], al)
    cnt += count(dr[d + 1], dc[d + 1], row + dr[d + 1], col + dc[d + 1], al)
    return cnt + 1

pan = [[*map(int, input().split())] for _ in range(19)]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
dr = [0, 0, 1, -1, 1, -1, -1, 1]
for c in range(19):
    for r in range(19):
        if pan[r][c] != 0:
            for i in range(0, 8, 2):
                if check(i, r, c, pan[r][c]) == 5:
                    print(pan[r][c])
                    print(r + 1, c + 1)
                    sys.exit(0)
print(0)