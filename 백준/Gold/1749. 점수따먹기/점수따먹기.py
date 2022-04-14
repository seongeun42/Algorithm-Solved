import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = [[0] * (M + 1)] + [[0] + [*map(int, input().split())] for _ in range(N)]
res = -10001
for i in range(1, N + 1):
    row = [0] * (M + 1)
    for j in range(i, N + 1):
        col = [0] * (M + 1)
        for k in range(1, M + 1):
            row[k] += nums[j][k]
            col[k] = max(col[k - 1] + row[k], row[k])
            res = max(res, col[k])
print(res)