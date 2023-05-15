import sys
input = sys.stdin.readline

n, h = map(int, input().split())
up = [0] * (h + 1)
down = [0] * (h + 1)

for i in range(n):
    height = int(input())
    if i % 2:
        down[height] += 1
    else:
        up[height] += 1

for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

ans = [n + 1, 0]
for i in range(1, h + 1):
    cnt = up[i] + down[h - i + 1]
    if cnt == ans[0]:
        ans[1] += 1
    elif cnt < ans[0]:
        ans = [cnt, 1]

print(*ans)