import sys
input = sys.stdin.readline

N = int(input())
ball = sorted([[i] + [*map(int, input().split())] for i in range(N)], key=lambda x: (x[2], x[1]))
prefix_sum = [0] * N
ans = [0] * N
color = [0] * (N + 1)
size = [0] * 2001
for i in range(N):
    prefix_sum[i] = prefix_sum[i - 1] + ball[i][2]
    if i > 0 and ball[i][1] == ball[i - 1][1] and ball[i][2] == ball[i - 1][2]:
        ans[ball[i][0]] = ans[ball[i - 1][0]]
    else:
        ans[ball[i][0]] = prefix_sum[i - 1] - color[ball[i][1]] - size[ball[i][2]]
    color[ball[i][1]] += ball[i][2]
    size[ball[i][2]] += ball[i][2]
print(*ans, sep="\n")