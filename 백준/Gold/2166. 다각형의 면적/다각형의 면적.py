import sys
input = sys.stdin.readline

N = int(input())
xy = [[*map(int, input().split())] for _ in range(N)]
xy.append(xy[0])
ans = 0
for i in range(N):
    ans += xy[i][0] * xy[i + 1][1] - xy[i + 1][0] * xy[i][1]
print(round(abs(ans) / 2, 1))