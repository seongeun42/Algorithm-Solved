import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def getCnt(x, y):
    cnt = 0
    tmp, i = 1, 0
    while i < N - 1:
        if B[y][i] != B[y][i + 1]:
            cnt = max(cnt, tmp)
            tmp = 1
        else:
            tmp += 1
            if i == N - 2:
                cnt = max(cnt, tmp)
        i += 1
    tmp, i = 1, 0
    while i < N - 1:
        if B[i][x] != B[i + 1][x]:
            cnt = max(cnt, tmp)
            tmp = 1
        else:
            tmp += 1
            if i == N - 2:
                cnt = max(cnt, tmp)
        i += 1
    return cnt

N = int(input())
B = [list(input().strip()) for _ in range(N)]
ans = 0
for i in range(N):
     for j in range(N):
          c = B[i][j]
          ans = max(ans, getCnt(j, i))
          for k in range(4):
               ni, nj = i + dy[k], j + dx[k]
               if 0 <= ni < N and 0 <= nj < N and B[ni][nj] != c:
                    B[ni][nj], B[i][j] = B[i][j], B[ni][nj]
                    ans = max(ans, getCnt(j, i))
                    B[ni][nj], B[i][j] = B[i][j], B[ni][nj]
print(ans)