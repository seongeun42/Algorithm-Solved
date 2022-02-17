import sys
input = sys.stdin.readline

R, C = map(int, input().split())
M = [list(input().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
alp = [0] * 26

def dfs(x, y, cnt):
    global res
    res = max(res, cnt)
    alp[ord(M[y][x]) - 65] = 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < C and 0 <= b < R:
            idx = ord(M[b][a]) - 65
            if not alp[idx]:
                dfs(a, b, cnt + 1)
                alp[idx] = 0

dfs(0, 0, 1)
print(res)