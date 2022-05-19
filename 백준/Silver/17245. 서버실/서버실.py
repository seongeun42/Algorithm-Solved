from _collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
loom = [[*map(int, input().split())] for _ in range(N)]
com = defaultdict(int)
total = sum(map(sum, loom))
l, r = 0, max(map(max, loom))
res = 0
for i in range(N):
    for j in range(N):
        if loom[i][j]:
            com[loom[i][j]] += 1

while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for k, v in com.items():
        cnt += k * v if k < mid else mid * v
    if cnt >= total / 2:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)